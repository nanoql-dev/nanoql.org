# SPDX-FileCopyrightText: 2026 The nanoql Authors
# SPDX-License-Identifier: Apache-2.0
"""Copy what the site takes from the library into _nanoql/, which git ignores.

Usage: python tools/sync.py <NanoQL checkout> --validation <results folder> [--source <URL prefix>] [--dirty]

The site's API reference, docs, generated pages, notices, conventions schema and home-page figures all come from one
NanoQL checkout, at the commit it has checked out:

- _nanoql/bin: NanoQL.dll and NanoQL.Extensions.dll with their XML documentation, built in Release, which docfx
  reads for the API reference;
- _nanoql/notices: the library's NOTICE and THIRD_PARTY_NOTICES.md, the latter without its title, for the licences
  page;
- _nanoql/schemas/conventions: nanoql-conventions.xsd, served at the conventions format's namespace;
- _nanoql/facts: one-line Markdown files the pages include: the commit, and the home page's validation figures;
- _nanoql/facts/first-swap-output.md: what the home page's example, examples/first-swap.cs, prints, compiled and run
  against the checkout, so the page's code is known to build and its output is the library's own;
- _nanoql/docs: what docfx builds under docs/. The library's versioned docs, its docs/ but the porting documents;
  their code samples, docs/examples' sources, copied beside them; and the samples' outputs, which that project
  writes into _generated/ when it runs. A link that leaves the imported docs, or that goes to an imported file docfx
  doesn't build (a sample's source, which carries its notice), goes to the file at the commit: --source's prefix,
  then the file's path in the checkout. Without --source, while the source's host is unnamed, the link's text stays
  and its target goes. Beside them, the site's own docs/index.md and docs/toc.yml, the
  navigation; and the pages the library's scripts write: the Excel function reference in excel/, by
  tools/docs/excel-reference.py from `nanoql-bind excel generate`'s sources, and extension-points.md, by
  tools/docs/extension-points.py from docfx's metadata of the two assemblies, which the sync runs first.
- _nanoql/validation/index.md: the validation report, by tools/docs/validation-report.py from --validation's
  results folder, a gates run's, and a checkout of the commit that folder names.

docfx resolves a link by its target's source, so the site's pages link to these pages by their paths here
(_nanoql/docs/getting-started.md), which it serves under docs/ and validation/.

The checkout's files the site shows must match its commit, so the site never shows what no commit holds; --dirty
previews uncommitted changes, the commit read as "<commit> with local changes".
"""
import re
import shutil
import subprocess
import sys
import tempfile

from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
OUT = SITE / "_nanoql"
ASSEMBLIES = ["NanoQL", "NanoQL.Extensions"]
NOTICES = ["NOTICE", "THIRD_PARTY_NOTICES.md"]
SCHEMA = "src/NanoQL.Extensions/Conventions/nanoql-conventions.xsd"
SHOWN = ["src", "docs", "tools/docs", "bindings/surface.json", "bindings/excel/functions.json",
         "bindings/excel/list.json", *NOTICES]
PORTING = {"docs/porting-plan.md", "docs/porting-map.md", "docs/porting-playbook.md"}
BUILT = {".md", ".yml"}  # docfx.json's content under docs/
EXAMPLE = SITE / "examples" / "first-swap.cs"
EXAMPLE_PROJECT = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  <ItemGroup>
    <ProjectReference Include="{nanoql}" />
  </ItemGroup>
</Project>
"""
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.I)


def run(args, cwd):
    done = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    if done.returncode != 0:
        sys.exit(f"{' '.join(map(str, args))} exited {done.returncode}:\n{done.stdout[-3000:]}{done.stderr[-3000:]}")
    return done.stdout


def python(script, *args, cwd):
    return run([sys.executable, "-I", str(script), *map(str, args)], cwd)


def listed(repo, *paths):
    """The checkout's files under the paths: its committed ones, and with --dirty its untracked ones too."""
    return run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", *paths], repo).splitlines()


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def option(argv, name):
    return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None


def import_docs(repo, source):
    """Copies the versioned docs and the examples' sources into _nanoql/docs, each link that leaves them rewritten.
    Returns the count of links rewritten and of links dropped."""
    docs = OUT / "docs"
    files = [f for f in listed(repo, "docs") if f not in PORTING and "/bin/" not in f and "/obj/" not in f]
    for f in files:
        target = docs / Path(f).relative_to("docs")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(repo / f, target)
    imported = {(docs / Path(f).relative_to("docs")).resolve() for f in files}
    counts, broken = {"rewritten": 0, "dropped": 0}, []
    for f in files:
        if not f.endswith(".md"):
            continue
        page = docs / Path(f).relative_to("docs")
        lines, fenced = page.read_bytes().decode("utf-8").split("\n"), False
        for i, line in enumerate(lines):
            if line.lstrip().startswith("```"):
                fenced = not fenced
            if fenced:
                continue

            def relink(m):
                text, href = m.group(1), m.group(2)
                path, _, fragment = href.partition("#")
                if not path or SCHEME.match(path):
                    return m.group(0)
                # docfx builds the imported pages and tables of contents, and an include ([!code-csharp[](…)])
                # reads any imported file; a link to another imported file would serve nothing.
                target = (page.parent / path).resolve()
                if target in imported and (target.suffix in BUILT or text.startswith("!")) or \
                        path.startswith("_generated/") or "/_generated/" in path:
                    return m.group(0)
                in_repo = (repo / f).parent / path
                if not in_repo.exists():
                    broken.append(f"{f}: {href}")
                    return m.group(0)
                rel = in_repo.resolve().relative_to(repo.resolve()).as_posix()
                if source:
                    counts["rewritten"] += 1
                    return f"[{text}]({source}{rel}{'#' + fragment if fragment else ''})"
                counts["dropped"] += 1
                return text

            lines[i] = LINK.sub(relink, line)
        page.write_bytes("\n".join(lines).encode("utf-8"))
    if broken:
        sys.exit("links to no file in the checkout:\n" + "\n".join(broken))
    for name in ("index.md", "toc.yml"):
        if (docs / name).exists():
            sys.exit(f"the library's docs/{name} would replace the site's")
        shutil.copy2(SITE / "docs" / name, docs / name)
    return counts


def main(argv):
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] not in
                                                                         ("--validation", "--source"))]
    validation, source = option(argv, "--validation"), option(argv, "--source")
    if len(args) != 1 or not validation:
        sys.exit(__doc__)
    repo, validation = Path(args[0]).resolve(), Path(validation).resolve()
    dirty = run(["git", "status", "--porcelain", "--untracked-files=all", "--", *SHOWN, SCHEMA], repo)
    if dirty and "--dirty" not in argv:
        sys.exit(f"{repo} has uncommitted changes the site would show (--dirty to preview them):\n{dirty}")
    commit = run(["git", "rev-parse", "HEAD"], repo).strip()[:7] + (" with local changes" if dirty else "")

    # The examples project references both assemblies, so its build gives the API reference's too.
    run(["dotnet", "build", "docs/examples", "-c", "Release"], repo)
    if OUT.exists():
        shutil.rmtree(OUT)
    built = repo / "src" / "NanoQL.Extensions" / "bin" / "Release" / "net10.0"
    for name in ASSEMBLIES:
        for ext in (".dll", ".xml"):
            (OUT / "bin").mkdir(parents=True, exist_ok=True)
            shutil.copy2(built / (name + ext), OUT / "bin" / (name + ext))
    for name in NOTICES:
        text = (repo / name).read_bytes().decode("utf-8")
        if name.endswith(".md") and text.startswith("# "):
            text = text.split("\n", 1)[1].lstrip("\n")  # the licences page gives the headings above it
        write(OUT / "notices" / name, text)
    (OUT / "schemas" / "conventions").mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo / SCHEMA, OUT / "schemas" / "conventions" / Path(SCHEMA).name)
    write(OUT / "facts" / "commit.md", commit + "\n")

    project = OUT / "example"
    write(project / "example.csproj", EXAMPLE_PROJECT.format(nanoql=repo / "src" / "NanoQL" / "NanoQL.csproj"))
    shutil.copy2(EXAMPLE, project / "Program.cs")
    run(["dotnet", "build", str(project), "-c", "Release"], repo)
    output = run(["dotnet", "run", "--no-build", "-c", "Release", "--project", str(project)], repo).strip()
    write(OUT / "facts" / "first-swap-output.md", f"```text\n{output}\n```\n")

    links = import_docs(repo, source)
    print(run(["dotnet", "run", "--no-build", "-c", "Release", "--project", "docs/examples", "--",
               str(OUT / "docs" / "_generated")], repo).strip())

    # The validation report reads the sources of the commit the gates ran on, which the results folder names, from a
    # checkout of it with LF line endings, as the gates' own; a short temporary path keeps its files under Windows'
    # path limit.
    docs = OUT / "docs"
    measured = (validation / "commit.txt").read_text(encoding="utf-8").strip()
    (OUT / "validation").mkdir(parents=True)
    with tempfile.TemporaryDirectory(prefix="nanoql-") as folder:
        checkout = Path(folder) / "measured"
        run(["git", "clone", "-q", "--shared", "--no-checkout", str(repo), str(checkout)], SITE)
        run(["git", "-c", "core.autocrlf=false", "-c", "core.eol=lf", "checkout", "-q", measured], checkout)
        print(python(repo / "tools" / "docs" / "validation-report.py", checkout, validation, "--page",
                     OUT / "validation" / "index.md", "--built-from", commit, "--home",
                     OUT / "facts" / "tested.md", cwd=repo).strip())

    sources = OUT / "excel-sources"
    run(["dotnet", "run", "--project", "src/NanoQL.Bind", "-c", "Release", "--", "excel", "generate", "--experimental",
         "--out", str(sources)], repo)
    print(python(repo / "tools" / "docs" / "excel-reference.py", sources, docs / "excel", "--root", repo,
                 cwd=repo).strip())
    pages = sorted((docs / "excel").glob("excel-*.md"))
    tasks = [p for p in pages if p.name not in ("excel-names.md", "excel-withheld.md")]
    write(docs / "excel" / "toc.yml", "".join(
        f"- name: {p.read_text(encoding='utf-8').split('# Excel functions: ', 1)[1].split(chr(10), 1)[0].capitalize()}"
        f"\n  href: {p.name}\n" for p in tasks) + "- name: Names in Excel\n  href: excel-names.md\n"
        "- name: Functions withheld\n  href: excel-withheld.md\n")

    run(["dotnet", "tool", "restore"], SITE)
    run(["dotnet", "docfx", "metadata", "docfx.json"], SITE)
    print(python(repo / "tools" / "docs" / "extension-points.py", SITE / "api", docs / "extension-points.md",
                 "--root", repo, cwd=repo).strip().split(";")[0])

    print(f"nanoql {commit}: the first swap prints {output}; links leaving the docs: {links['rewritten']} rewritten, "
          f"{links['dropped']} dropped")


if __name__ == "__main__":
    main(sys.argv[1:])
