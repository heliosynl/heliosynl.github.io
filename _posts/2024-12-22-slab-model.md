---
title: "Slab Surface Modeling by Atomsk and VESTA"
date: 2024-12-22
excerpt: 'Slab surface modeling by using Atomsk and VESTA, in Quantum Espresso PWscf format'
permalink: /posts/2024/blog1222/
type: blog
tags:
  - Ab Initio
  - Modeling
  - blog
---
# Atomic Modeling
Structural optimizing **bulk model** first.

can use model converter such as [Atomsk](https://atomsk.univ-lille.fr/) to convert optimized file in [VESTA](https://jp-minerals.org/vesta/en/) format

```sh
atomsk model.scf.in vesta
```

Atomsk is an open-sourced command-line modeling code. VESTA is an open-source atomic model visualization code. Open the model in .vesta format with VESTA can get
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiCbulk.png' width=400>

For example, a 4H-SiC (0001) 1x1x2 slab model is building, vacuum at the z direction.
## Duplicate unit cell
- Edit-Edit Data-Unit cell
- Transform
- Multiply the diagonal element by the multiplier needed, 1 1 2 here
- Notification windows not important
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiC112.png' width=400>

## Include the topmost atomic layer and Remove the repetitive atoms
- Objects-Boundary
- x(max) and y(max) take value slightly **smaller** than 1 (e.g. 0.9)
- z(max) takes value slightly **bigger** than 1 (e.g. 1.1)
- confirm whether (1) additional atomic layer is added (2) extra atoms at the boundary are removed
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiCboundary.png' width=400>

## Remove extra atoms bonded
- Edit-Bonds
- Boundary mode-Do not search atoms beyond the boundary
  - usually Max. length 2.4 can see bonds (empirical)
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiCbonds.png' width=400>

After these, a simplier 1x1x2 model was get.

## Convert to PWscf format
Before output, go `View along the c axis` and check **No external** atoms exist
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiCcaxis.png' width=400>
- File-Export Data
- in `.xyz` format
- Dont save hidden atoms

get `.xyz` file like

```
18
# title
Si    0.000000    0.000000    0.630051
Si    0.000000    0.000000   20.859656
Si    0.000000    0.000000   10.744853
Si    0.000003    1.789389    5.687452
Si    0.000003    1.789389   15.802255
Si    1.549659    0.894694    3.158033
Si    1.549659    0.894694   13.272836
Si    1.549659    0.894694    8.215435
Si    1.549659    0.894694   18.330237
 C    0.000000    0.000000    2.535659
 C    0.000000    0.000000   12.650462
 C    0.000003    1.789389    7.593061
 C    0.000003    1.789389   17.707863
 C    1.549659    0.894694    5.057452
 C    1.549659    0.894694   15.172254
 C    1.549659    0.894694    0.000000
 C    1.549659    0.894694   20.229605
 C    1.549659    0.894694   10.114853
```

check again the coordinates and number of atoms.

To guarantee the lattice parameter at x y direction, save the VESTA file, convert to PWscf input by atomsk again

```sh
atomsk model.scf.vesta pw
```

Last step, change `nat` and `ATOMIC_POSITIONS angstrom` to content in .xyz file, **adjust cell length in z direction** to include vacuum layer.

- Can use [AtomicPos](/codes/atomicpos/) to adjust atomic position
  - can make the model align to the cell center
    - z-coordinates + half length of vacuum layer
- If polar system/orientation, need to add pseudo-Hydrogen atoms. See more in [PseudoHPseudopot](/about/) and [PolarSurface](/about/)
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiCslab.png' width=400>