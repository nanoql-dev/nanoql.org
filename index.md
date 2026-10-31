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
<a href="docs/getting-started.md">Get started</a>
<a href="migration/index.md">Migrating to nanoql</a>
<a href="https://github.com/nanoql-org/nanoql">GitHub</a>
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

Every result in the core is checked against independent reference values to a relative <span class="text-nowrap">1e-10</span>:
[!include[tests](_nanoql/facts/tests.md)] tests over [!include[vectors](_nanoql/facts/vectors.md)] committed test-vector files.

</div>
</div>

</div>
