# SPDX-FileCopyrightText: 2026 The nanoql Authors
# SPDX-License-Identifier: Apache-2.0
"""Copy what the site takes from the library into _nanoql/, which git ignores.

Usage: python tools/sync.py <NanoQL checkout> [--no-tests] [--dirty]

The site's API reference, notices, conventions schema and home-page figures all come from one NanoQL checkout, at the
commit it has checked out:

- _nanoql/bin: NanoQL.dll and NanoQL.Extensions.dll with their XML documentation, built in Release, which docfx
  reads for the API reference;
- _nanoql/notices: the library's NOTICE and THIRD_PARTY_NOTICES.md, the latter without its title, for the licences
  page;
- _nanoql/schemas/conventions: nanoql-conventions.xsd, served at the conventions format's namespace;
- _nanoql/facts: one-line Markdown files the pages include: the commit, and the counts of committed test-vector files
  and tests (the hundreds, rounded down);
- _nanoql/facts/first-swap-output.md: what the home page's example, examples/first-swap.cs, prints, compiled and run
  against the checkout, so the page's code is known to build and its output is the library's own.

The checkout's src/ and the files copied from it must match its commit, so the site never shows code that no commit
holds; --dirty previews uncommitted changes, the commit read as "<commit> with local changes". --no-tests skips
building and listing the test project, and the tests figure reads "–".
"""
import shutil
import subprocess
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
OUT = SITE / "_nanoql"
ASSEMBLIES = ["NanoQL", "NanoQL.Extensions"]
NOTICES = ["NOTICE", "THIRD_PARTY_NOTICES.md"]
SCHEMA = "src/NanoQL.Extensions/Conventions/nanoql-conventions.xsd"
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


def run(args, cwd):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True, encoding="utf-8").stdout


def tracked(repo, *paths):
    return run(["git", "ls-tree", "-r", "--name-only", "HEAD", "--", *paths], repo).splitlines()


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    repo = Path(args[0]).resolve()
    tests = "--no-tests" not in argv
    dirty = run(["git", "status", "--porcelain", "--untracked-files=no", "--", "src", SCHEMA, *NOTICES], repo)
    if dirty and "--dirty" not in argv:
        sys.exit(f"{repo} has uncommitted changes the site would show (--dirty to preview them):\n{dirty}")
    commit = run(["git", "rev-parse", "HEAD"], repo).strip()[:7] + (" with local changes" if dirty else "")

    run(["dotnet", "build", "NanoQL.slnx" if tests else "src/NanoQL.Extensions", "-c", "Release"], repo)
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

    vectors = len(tracked(repo, "tests/vectors"))
    count = "–"
    if tests:
        listing = run(["dotnet", "test", "--solution", "NanoQL.slnx", "-c", "Release", "--no-build", "--list-tests"],
                      repo)
        # The listing names each case; a run can count a few more, so the page gives the hundreds, rounded down.
        listed = sum(1 for line in listing.splitlines() if line.strip().startswith("NanoQL.Tests."))
        count = f"{listed // 100 * 100:,}+"
    facts = {"commit": commit, "vectors": f"{vectors:,}", "tests": count}
    for name, value in facts.items():
        write(OUT / "facts" / f"{name}.md", value + "\n")

    project = OUT / "example"
    write(project / "example.csproj", EXAMPLE_PROJECT.format(nanoql=repo / "src" / "NanoQL" / "NanoQL.csproj"))
    shutil.copy2(EXAMPLE, project / "Program.cs")
    run(["dotnet", "build", str(project), "-c", "Release"], repo)
    output = run(["dotnet", "run", "--no-build", "-c", "Release", "--project", str(project)], repo).strip()
    write(OUT / "facts" / "first-swap-output.md", f"```text\n{output}\n```\n")
    print(f"nanoql {commit}: " + ", ".join(f"{k} {v}" for k, v in facts.items() if k != "commit"))
    print(f"the first swap prints: {output}")


if __name__ == "__main__":
    main(sys.argv[1:])
