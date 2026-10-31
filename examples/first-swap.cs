using NanoQL;
using NanoQL.Indexes;
using NanoQL.Instruments;
using NanoQL.PricingEngines;
using NanoQL.TermStructures;
using NanoQL.Time;

var today = new Date(15, Month.October, 2026);
var context = new EvaluationContext { EvaluationDate = today };
var curve = new FlatForward(today, 0.036, new Actual365Fixed());

var swap = new MakeOIS(new Period(5, TimeUnit.Years), new Sofr(curve))
    .WithFixedRate(0.036).WithNominal(10e6)
    .ToOvernightIndexedSwap(context);

var result = DiscountingSwapEngine.Calculate(swap, context, curve);
Console.WriteLine($"NPV {result.NPV:N2}, fair rate {result.FairRate:P4}");
