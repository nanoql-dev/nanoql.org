---
_layout: landing
title: Quantitative finance, stateless by design
---

<div class="nq-band">
<div class="nq-band-inner">

# Quantitative finance,<br class="nq-break"> stateless by design.

Rates, credit, equity, FX, inflation and commodities, vanilla to exotic. Every pricer is a plain function of its
inputs, and market conventions are data you can override. From C#, Python, C++ and Excel.

<div class="nq-band-actions">
<a href="_nanoql/docs/getting-started.md">Get started</a>
<a href="migration/index.md">Migrating to nanoql</a>
<a href="https://github.com/nanoql-dev/nanoql">GitHub</a>
</div>

</div>
</div>

<div class="nq-body">

## A first swap

Install the package:

<div class="nq-shell">

```shell
dotnet add package NanoQL
```

</div>

Then price a five-year SOFR swap on a flat curve. The curve, the swap and the evaluation date are values, and the
engine is a function of them:

[!code-csharp[](examples/first-swap.cs)]

It prints:

<div class="nq-output">

[!include[output](_nanoql/facts/first-swap-output.md)]

</div>

Prefer Python? [Run this and more in your browser](https://colab.research.google.com/github/nanoql-dev/nanoql/blob/main/docs/notebooks/first-steps.ipynb): curves, SABR, options and CDS.

## Why nanoql

<div class="nq-why">
<div>

### Stateless

Instruments, curves and models are immutable values, pricers are static functions of them, and the evaluation date
is an argument, not a global setting. The same inputs always give the same outputs, and calls run side by side.

</div>
<div>

### Conventions as data

Calendars, day counts, currencies, indexes and the instrument builders' defaults are XML records: read them,
override them for a desk, and version them with your trades.

</div>
<div>

### Tested

Checked against [!include[tested](_nanoql/facts/tested.md)]
[The validation report](_nanoql/validation/index.md) has the figures, [the divergences page](_nanoql/docs/divergences.md)
each departure.

</div>
<div>

### C#, Python, C, C++ and Excel

From C# and F#, and from Python, C and [C++](_nanoql/docs/cpp.md) through one C interface over nanoql compiled to native
code: `pip install nanoql` needs no .NET runtime, and the C archive serves any language that calls C. In Excel on
Windows, [an add-in](_nanoql/docs/excel.md) puts the library in worksheet formulas.

</div>
</div>

</div>
