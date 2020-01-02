# dataviz

Visualise data the easy way, with sane defaults.

**Note:** This package is work in (extremely slow) progress! Stage: $\alpha$!

This package shall at one point provide you with the right tools to do the following:

1. Import your data from almost everywhere.
2. Easily perform scientific calculations with uncertainties and units.
3. Visualise your work with error bars and fits

## Implementation order

### Units

The unit system is a good point to start with, because it should have all of the following:

+ understanding of your input: Use the units you like (imperial, metric, with prefixes).
+ under–the–hood converter tools (do the calculations with SI units internally).
+ unit simplification: $5~\mathrm{kg}\cdot 2\frac{\mathrm{m}}{\mathrm{s}^2}$ should give you $10~\mathrm{N}$, not $10\frac{\mathrm{kg~m}}{\mathrm{s}^2}$.

Most unit system implementation have the first two properties, but they lack the last one. A good test is to combine a ton of units and see if you get more of them back than the number of base units:  
$$
1=\frac{\mathrm{J~C~mol~Sv~H}}{\mathrm{N~m}^3~\mathrm{s}^2~\mathrm{Gy~T~kat~\Omega~S}}
$$  
It is rather obvious that 1 means a dimensionless quantity (amount), whereas it is not obvious that the right hand side is dimensionless.

Esoteric units in the above formula:

+ $\mathrm{Gy}$: Gray
+ $\mathrm{S}$: Siemens
+ $\mathrm{Sv}$: Sievert

This is (hopefully) enough to convince you that the unit simplification is one of the most important aspects of the implementation.