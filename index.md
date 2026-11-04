---
_layout: landing
title: Quantitative finance for .NET
---

<div class="nq-band">
<div class="nq-band-inner">

# Quantitative finance for .NET,<br class="nq-break"> stateless by design.

nanoql prices rates, credit, equity, FX, inflation and commodity products. Every pricer is a plain function of its
inputs, and market conventions are data you can override.

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

## Why nanoql

<div class="nq-why">
<div>

### Stateless

Instruments, curves and models are immutable values, and pricers are static functions of them. The same inputs
always give the same outputs, and calls run side by side.

</div>
<div>

### Conventions as data

Calendars, day counts, currencies, indexes and the instrument builders' defaults are XML records: read them,
override them for a desk, and version them with your trades.

</div>
<div>

### Tested

Results are checked against independent reference values: [!include[tested](_nanoql/facts/tested.md)]
[The validation report](_nanoql/validation/index.md) gives the figures by module.

</div>
<div>

### Python and C

From C# and F#, and from Python and C through one C interface over nanoql compiled to native code:
`pip install nanoql` needs no .NET runtime, and the C archive serves any language that calls C.

</div>
</div>

</div>
