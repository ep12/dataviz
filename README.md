# dataviz

Visualise data the easy way, with sane defaults.

**Note:** This package is work in (extremely slow) progress! Stage: ![\alpha](https://latex.codecogs.com/svg.latex?\inline%20%5Calpha)!

This package shall at one point provide you with the right tools to do the following:

1. Import your data from almost everywhere.
2. Easily perform scientific calculations with uncertainties and units.
3. Visualise your work with error bars and fits

## Implementation order

### Units

The unit system is a good point to start with, because it should have all of the following:

+ understanding of your input: Use the units you like (imperial, metric, with prefixes).
+ under–the–hood converter tools (do the calculations with SI units internally).
+ unit simplification: ![5~\mathrm{kg}\cdot 2\frac{\mathrm{m}}{\mathrm{s}^2}](https://latex.codecogs.com/svg.latex?\inline%205~%5Cmathrm%7Bkg%7D%5Ccdot+2%5Cfrac%7B%5Cmathrm%7Bm%7D%7D%7B%5Cmathrm%7Bs%7D%5E2%7D) should give you ![10~\mathrm{N}](https://latex.codecogs.com/svg.latex?\inline%2010~%5Cmathrm%7BN%7D), not ![10\frac{\mathrm{kg~m}}{\mathrm{s}^2}](https://latex.codecogs.com/svg.latex?\inline%2010%5Cfrac%7B%5Cmathrm%7Bkg~m%7D%7D%7B%5Cmathrm%7Bs%7D%5E2%7D).

Most unit system implementation have the first two properties, but they lack the last one. A good test is to combine a ton of units and see if you get more of them back than the number of base units:  
![1=\frac{\mathrm{J~C~mol~Sv~H}}{\mathrm{N~m}^3~\mathrm{s}^2~\mathrm{Gy~T~kat~\Omega~S}}](https://latex.codecogs.com/svg.latex?1%3D%5Cfrac%7B%5Cmathrm%7BJ~C~mol~Sv~H%7D%7D%7B%5Cmathrm%7BN~m%7D%5E3~%5Cmathrm%7Bs%7D%5E2~%5Cmathrm%7BGy~T~kat~%5COmega~S%7D%7D)  
It is rather obvious that 1 means a dimensionless quantity (amount), whereas it is not obvious that the right hand side is dimensionless.

Esoteric units in the above formula:

+ ![\mathrm{Gy}](https://latex.codecogs.com/svg.latex?\inline%20%5Cmathrm%7BGy%7D): Gray
+ ![\mathrm{S}](https://latex.codecogs.com/svg.latex?\inline%20%5Cmathrm%7BS%7D): Siemens
+ ![\mathrm{Sv}](https://latex.codecogs.com/svg.latex?\inline%20%5Cmathrm%7BSv%7D): Sievert

This is (hopefully) enough to convince you that the unit simplification is one of the most important aspects of the implementation.
