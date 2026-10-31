# nanoql and Masseef

Masseef sponsors nanoql and maintains it.

## How Masseef uses nanoql

Masseef's platform prices through nanoql. It calls nanoql's public API from adapters behind its own pricing
interface: the trade, its market data and its conventions go in, the results come out, and nothing is held between
calls. Because nanoql's pricers are stateless, the platform can reprice a trade as of any past date, and revalue a
portfolio in parallel, with the same results each time.

## What stays open

- nanoql is complete on its own: nothing in it depends on Masseef, and it needs no Masseef product to run.
- Fixes Masseef makes to nanoql are made in nanoql's public repository, under the same licence and the same review
  as anyone's.
- nanoql stays under the Apache License 2.0.
