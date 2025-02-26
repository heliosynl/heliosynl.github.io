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

Content
=====
{:.no_toc}

* toc
{:toc}

# Atomic modeling
Structural optimizing **bulk model** first. All the following operations are based on the relaxed **bulk model unit cell** (`vc-relax` is better, to optimize both lattice parameter and atomic coordinates).

can use model converter such as [Atomsk](https://atomsk.univ-lille.fr/) to convert optimized file in [VESTA](https://jp-minerals.org/vesta/en/) format

```sh
atomsk model.scf.in vesta
```

Atomsk is an open-sourced command-line modeling code. VESTA is an open-source atomic model visualization code. Open the model in .vesta format with VESTA can get

![bulk](/images/notes/2024-12-22-slab-model/4H-SiCbulk.png)

For example, a 4H-SiC (0001) 1x1x2 slab model is building, vacuum at the z direction.
## Duplicate unit cell
- Edit-Edit Data-Unit cell
- Transform
- Multiply the diagonal element by the multiplier needed, 1 1 2 here
- Notification windows not important

![112](/images/notes/2024-12-22-slab-model/4H-SiC112.png)

## Include the topmost atomic layer and Remove the repetitive atoms
- Objects-Boundary
- x(max) and y(max) take value slightly **smaller** than 1 (e.g. 0.9)
- z(max) takes value slightly **bigger** than 1 (e.g. 1.1)
- confirm whether (1) additional atomic layer is added (2) extra atoms at the boundary are removed

![boundary](/images/notes/2024-12-22-slab-model/4H-SiCboundary.png)

## Remove extra atoms bonded
- Edit-Bonds
- Boundary mode - Do not search atoms beyond the boundary
  - usually Max. length 2.4 can see bonds (empirical), for metallic bond 2.6

![bonds](/images/notes/2024-12-22-slab-model/4H-SiCbonds.png)

After these, a simplier 1x1x2 model was get.

## Convert to PWscf format
Before output, go `View along the c axis` and check **No external** atoms exist

![caxis](/images/notes/2024-12-22-slab-model/4H-SiCcaxis.png)
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

![slab](/images/notes/2024-12-22-slab-model/4H-SiCslab.png)

# Model illustrating
To format the model illustration, can follow the below step

## Convert slab model from scf (relaxed) to vesta
```sh
atomsk model.scf.in vesta
```

same to the first step

## Remove no needed widget and formating
Open `model.scf.vesta` in VESTA first
- Objects - Properties - General
  - Axes - **No** show compass
  - Atoms - Material - Specular: 0 0 0 Shininess 100
  - Bonds - Material - Specular: 130 130 130 Shininess 80
- Objects - Boundary
  - increase/decrease (max)/(min) if needed, to show more atoms
  - usually dont modify z axis (for vacuum layer at z direction)
- Edit - Bonds
  - For C-termination
    - Search mode - Search atoms bonded to A1
    - Boundary mode - Search additional atoms if A1 is included in the boundary
    - A1 - atoms other than C (surface atoms)
    - usually Max. length 2.4 can see bonds (empirical), for metallic bond 2.6
- View along the a* axis
- Rotate 90 degree
  - let the interested surface heading **left**
- (if need) Fit to the screen
  - Zoom in to have better size

## Output .png file with transparent background
**Only Windows VESTA can output TRANSPARENT PNG!!**

The output figure will be the same size of the VESTA window, can shrink the window before outputing, to have narrow/wide figure.

- File - Export Raster Image
  - modify file name, no .scf, .png format
  - Scale 4 (empirical)
  - Let the background transparent

Wide figure:

![slabC](/images/notes/2024-12-22-slab-model/4H-SiCslabC.png)

Narrow figure (Square figure here):

![222slab](/images/notes/2024-12-22-slab-model/z011-222slab.png)
