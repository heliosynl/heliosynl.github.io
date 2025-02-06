---
title: "Polar surface slab model"
date: 2024-12-20
excerpt: 'Quantum Espresso PWscf polar slab model'
# permalink: /posts/2024/blog1224/
type: record #blog
tags:
  - Ab Initio
  - Quantum Espresso
  - PWscf
  - record #blog
---

Content
=====
{:.no_toc}

* toc
{:toc}

# NJP2010_A comparative DFT study of electronic properties
SiC surface slab modeling
## Atomic modeling
MOSFET, the role of electric field and the influence of stacking sequence to the surface electronic and structural properties, for 2H- 4H- 6H-SiC

thick slab simulations, one model have 6-18 SiC double layers, that is, no more than 36 atoms in one unit cell.

It is said that, surface relaxation doesn't induce too much atomic shifts (or the impact depth is less than *1* unit cell), so we can use (1x1) supercells to consider the surface relaxation.
> The fact that SiC(0001) Si-terminated and SiC(000-1) C-terminated surfaces can be prepared **without surface reconstruction**, (1x1) supercells were employed.

Take (0001) Si-terminated case for instance, the bottommost atomic layer is C atoms. Two cases have been considered, terminated by hydrogen atoms, and have broken bonds (surface relaxation at C-terminated face also). Also include **dipole correction** to prevent artificial electrostatic field.
> Due to the fact that significant relaxation is limited to **the first two layers**, in other cases only two layers were relaxed.

## ZnO dipole, polarization field
> Meyer and Marx [30] claimed that the ZnO surface can be described using the purely ionic model, where each ZnO DL exhibits a dipole moment perpendicular to the surface. In such a model we obtain spontaneous polarization, which is independent of the thickness of the slab. In such a model we obtain spontaneous polarization, which is independent of the thickness of the slab.

if **spontaneous polarization** is *independent* of the thickness of the slab, my assumption may be violated!

Potential distribution showed the **independency** of slab thickness (Fig.3), they proposed that 
> the field inside the slab is **smaller** for **larger thickness** and there is divergence for large thickness. So the purely ionic model is unstable and has to be corrected. The electron density at the ends of slab *decrease* for *thicker* surface.

## potential field distribution and reasoning
The potential distribution can be divided into two parts, linear part and nonlinear part. The linear part is in accordance with the previous prediction. Due to the spontaneous charge separation (charge transfer) between two polar ends, similar to the case of ZnO surfaces. This charge separation can be seen as the opposite sign of charge accumulation at each end, in valence band and conduction band, leading to the linear uniform electric field inside the slab. But this prediction is **unstable**, especially for thick slab, causing divergence: the field will not be constant anymore. Instead, only **the difference in potential** between both the sides is *preserved*. That's the reason of smaller electric field for thicker slab.

# npjCM2021_Finite-size correction for slab supercell 
if interested in O face, use 1.5 valence pseudo-H on the opposite 