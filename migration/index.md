# Migrating to nanoql

nanoql's types follow QuantLib's, so code written against QuantLib-Python or QLNet maps class by class. Each guide
pairs that code with nanoql's for the rates products, and states what changes: the evaluation date, quotes and
handles, engines and fixings.

- [From QuantLib-Python](../_nanoql/docs/migration/from-quantlib-python.md)
- [From QLNet](../_nanoql/docs/migration/from-qlnet.md)

Each class and function QuantLib-Python constructs, and each QuantLib class nanoql ports, has its nanoql form in a
table:

- [QuantLib-Python's constructions](../_nanoql/docs/parity/quantlib-python.md)
- [QLNet's classes](../_nanoql/docs/parity/qlnet.md)
