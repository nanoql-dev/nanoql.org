# Documentation

- [Getting started](getting-started.md): the package and a first swap.
- [Concepts](concepts.md): values and functions, the evaluation context, conventions as data.
- [The stateless design](stateless.md): rebuilding on change, memoizing, pricing scenarios in parallel, valuing as of a
  past date.

## Rates

- [Dates and calendars](rates/dates-and-calendars.md)
- [Curves](rates/curves.md)
- [Multi-curve bootstrapping](rates/multi-curve.md): an €STR curve for discounting, and Euribor 6M bootstrapped on it.
- [Indexes and fixings](rates/indexes-and-fixings.md)
- [Swaps](rates/swaps.md)
- [Basis swaps and FX](rates/basis-and-fx.md): a basis swap, an FX forward, curves from FX swap points and
  cross-currency basis swaps.
- [Caps and floors](rates/caps-and-floors.md)
- [Swaptions](rates/swaptions.md)
- [A SABR smile](rates/sabr.md): a swaption smile fitted by SABR, and the smile section an engine reads.
- [Short-rate models](rates/short-rate-models.md): G2 and Hull-White calibrated to swaptions, and a Bermudan swaption.
- [Pricing a USD SOFR swap to match the market](sofr-example.md)

## Equity

- [Equity options](equity/options.md): one put, European, Bermudan and American, by each engine family.
- [A volatility surface and Heston's calibration](equity/volatility-and-heston.md)

## Credit

- [Credit default swaps](credit/cds.md): a hazard curve from spreads, and ISDA's standard model.

## Conventions

- [Market conventions as data](conventions.md): the XML format and convention sets.
- [The conventions catalogue](conventions-catalogue.md): every value the library ships.

## Beyond C\#

- [The bindings](bindings.md): Python and C, which any language that calls C can use.
- [The Excel add-in](excel.md), with its functions listed by task under Excel.

## Reference

- The [API reference](~/api/index.md) covers every public type.
- [Extension points](extension-points.md): the bases and interfaces your own types derive from.
