# About nanoql

nanoql is an open-source library for quantitative finance on .NET, under the Apache License 2.0. Its models, curves
and pricers are plain functions of immutable inputs, and its market conventions are data.

## Where it comes from

nanoql builds on open-source work, and every file it ports records where from:

- **QuantLib.** nanoql's core is derived from QuantLib 1.44, and its results are checked against QuantLib's own.
  Its design differs: it has no observers, lazy objects or global evaluation date. Where porting finds a defect,
  nanoql usually fixes it, and each place its results depart from QuantLib's is documented in
  [Divergences](../validation/divergences.md).
- **QLNet.** nanoql's extensions port QLNet's mortgage-backed securities, with their prepayment models, and its
  amortised-cost bonds, checked against QLNet 1.13.2.
- **FpML.** nanoql's conventions files accept the codes of FpML's coding schemes, such as its day-count and
  business-centre codes, beside nanoql's own names.

Their copyright notices and licences are on [Licences and notices](licenses.md). nanoql is an independent project:
the QuantLib and QLNet projects, and ISDA, which publishes FpML, are not affiliated with it and don't endorse it.

## Who maintains it

nanoql is sponsored and maintained by Masseef ([nanoql and Masseef](masseef.md)). It is developed in the open on
[GitHub](https://github.com/nanoql-org/nanoql): anyone can report an issue, ask in its Discussions, or send a pull
request, signed off under the
[Developer Certificate of Origin](https://github.com/nanoql-org/nanoql/blob/main/CONTRIBUTING.md).

## Contact

- Questions and ideas: [GitHub Discussions](https://github.com/nanoql-org/nanoql/discussions).
- Security reports: see [Security](security.md).
- The code of conduct: conduct@nanoql.org.
