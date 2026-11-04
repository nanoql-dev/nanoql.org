# nanoql.org

The source of [nanoql.org](https://nanoql.org), the website of [nanoql](https://github.com/nanoql-dev/nanoql), built
with [docfx](https://dotnet.github.io/docfx/).

## Building it

It needs the .NET 10 SDK, Python 3, a nanoql checkout and the results folder of a gates run on it. The guides, the
API reference, the generated pages, the notices, the conventions schema and the home page's figures come from that
checkout, at the commit it has checked out:

```shell
python tools/sync.py ../NanoQL --validation <results>   # builds nanoql, runs its docs' scripts, fills _nanoql/
dotnet tool restore                 # docfx, pinned in dotnet-tools.json
dotnet docfx docfx.json --warningsAsErrors
dotnet docfx serve _site            # http://localhost:8080
```

A broken link or cross-reference fails the build. `tools/sync.py` documents its inputs and what it writes.

## Layout

| Path | What |
|---|---|
| `index.md` | The home page |
| `examples/` | The home page's example, which `tools/sync.py` compiles and runs against nanoql for the output it shows |
| `docs/`, `migration/`, `validation/` | The navigation over nanoql's guides, migration guides and validation report, which the sync imports from the checkout |
| `api/` | The API reference, generated from nanoql's assemblies and their XML documentation |
| `about/` | About nanoql, Masseef, related projects, security, licences |
| `schemas/conventions/` | The page at the conventions format's namespace, beside its schema |
| `brand/` | The wordmark, the mark and the icons; `brand/README.md` holds their rules |
| `template/` | The site's colours and scripts over docfx's modern template |

## Licence

Apache 2.0, see [LICENSE](LICENSE). The wordmark's letters are drawn from Space Grotesk, under the SIL Open Font
License 1.1 (`brand/README.md`).
