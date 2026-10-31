# Related projects

## QuantLib

[QuantLib](https://www.quantlib.org/) is the free, open-source C++ library for quantitative finance. nanoql's core
is derived from QuantLib 1.44, and the core's results are checked against QuantLib's: QuantLib's Python package and
its C++ build generate the test vectors nanoql commits.

## QLNet

[QLNet](https://github.com/amaggiulli/QLNet) is a C# financial library derived from QuantLib. nanoql's extensions
port its additions for the bond market, mortgage-backed securities with prepayment models and amortised-cost bonds,
checked against QLNet 1.13.2.

Neither project is affiliated with nanoql or endorses it.
