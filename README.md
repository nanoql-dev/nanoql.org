# nanoql.org

The source of [nanoql.org](https://nanoql.org), the website of [nanoql](https://github.com/nanoql-org/nanoql), built
with [docfx](https://dotnet.github.io/docfx/).

## Building it

It needs the .NET 10 SDK, Python 3 and a nanoql checkout. The API reference, the notices, the conventions schema
and the home page's figures come from that checkout, at the commit it has checked out:

```shell
python tools/sync.py ../NanoQL      # builds nanoql and copies what the site reads into _nanoql/
dotnet tool restore                 # docfx, pinned in dotnet-tools.json
dotnet docfx docfx.json --warningsAsErrors
dotnet docfx serve _site            # http://localhost:8080
```

A broken link or cross-reference fails the build.

## Layout

| Path | What |
|---|---|
| `index.md` | The home page |
| `examples/` | The home page's example, which `tools/sync.py` compiles and runs against nanoql for the output it shows |
| `docs/`, `migration/`, `validation/` | The guides, the migration guide, the validation report |
| `api/` | The API reference, generated from nanoql's assemblies and their XML documentation |
| `about/` | About nanoql, Masseef, related projects, security, licences |
| `schemas/conventions/` | The page at the conventions format's namespace, beside its schema |
| `brand/` | The wordmark, the mark and the icons; `brand/README.md` holds their rules |
| `template/` | The site's colours and scripts over docfx's modern template |

## Licence

Apache 2.0, see [LICENSE](LICENSE). The wordmark's letters are drawn from Space Grotesk, under the SIL Open Font
License 1.1 (`brand/README.md`).
