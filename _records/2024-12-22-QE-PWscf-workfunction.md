---
title: "QE PWscf Slab Work Function"
date: 2024-12-22
excerpt: 'Quantum Espresso PWscf slab model work function calculation'
# permalink: /posts/2024/blog1224/
type: records #blog
tags:
  - Ab Initio
  - Quantum Espresso
  - PWscf
  - records #blog
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
- If polar system/orientation, need to add pseudo-Hydrogen atoms. See more in [PseudoHPseudopot](/records/2024-12-10-PseudoH-Pseudopot) and [PolarSurface](/records/2024-12-20-polar-surface-slab)
<br/><img src='/images/notes/2024-12-22-QE-PWscf-Workfunction/4H-SiCslab.png' width=400>

# 0. structural optimization, kpt convergence, ecut convergence, smearing convergence
**Do before any calculation**
# 1. scf

# 2. nscf

# 3. electronstatic potential postprocessing
`pp.x`

```
&inputpp
  prefix = '4HSiC'
  outdir = './calout'
  filplot = '4H-SiCslabSi_pot' ! file saving charge density in qe format
  plot_num=  11 ! Differential charge density 9, electrostatic potential (V_bare + V_H) 11, ELF 8
/

! Below no need, only need in 3D file outputing
! &plot
!   nfile = 1
!   iflag = 3 ! 3D ploting
!   output_format = 6 ! Can be read by VESTA
!   fileout = 'charge.prefix.cube' ! Can be read by VESTA
!   e1(1)=1.0,e1(2)=0.0,e1(3)=0.0,
!   e2(1)=0.0,e2(2)=1.0,e2(3)=0.0,
!   e3(1)=0.0,e3(2)=0.0,e3(3)=1.0,
!   x0(1)=1.0,x0(2)=0.0,x0(3)=0.0,
!   nx=101,ny=101,nz=2001
!   ! e1 e2 e3 plotting parallelepiped vectors
!   ! x0 origin of the parallelepiped
!   ! nx ny nz number of points in the parallelepiped
! /

```

Producing `4H-SiCslabSi_pot`

# 4. Averge on planes
`average.x` remember **Dont use MPI**

```
1                   ! number of 3D-FFT files
4H-SiCslabSi_pot    ! name of 3D-FFT files
1.0                 ! weight of 3D-FFT files
2000                ! number of points in the mesh
3                   ! direction, defining the planar average (planes perpendicular to this direction)
5.35255070433784    ! macroscopic averege length, in Bohr, usually one unit cell length, not important if do other post-processing with python
```

Producing `avg.dat`, including three columns

```
    position(Bohr) RAW planar    averaged planar
    0.000000000    0.461792073    0.461791837
    0.024566440    0.461820901    0.461790631
    0.049132879    0.461840212    0.461789673
    0.073699319    0.461843995    0.461789148
    0.098265758    0.461831147    0.461789104
    0.122832198    0.461805756    0.461789441
    0.147398638    0.461775773    0.461789942
    0.171965077    0.461750488    0.461790347
    0.196531517    0.461737628    0.461790430
    0.221097957    0.461740962    0.461790069
    0.245664396    0.461759172    0.461789281
    0.270230836    0.461786318    0.461788213
    0.294797275    0.461813735    0.461787095
    0.319363715    0.461832762    0.461786168
    0.343930155    0.461837443    0.461785608
    0.368496594    0.461826349    0.461785476
    0.393063034    0.461802988    0.461785700
    0.417629474    0.461774657    0.461786101
    ...
```

gnuplot: 
can also find Fermi level then plot with, found in `nscf.out` by `grep Fermi nscf....out`, length can be obtain by the last row first column in `tail avg.dat`

```sh
gnuplot -p -e "plot 'avg.dat' w l, 'avg.dat' u 1:3 w l, [0:49.108312808] 2.3868 w l t 'Fermi level'"
```

![Pot](/images/notes/2024-12-22-QE-PWscf-Workfunction/SihaveHpot.png)

# 5. Python planar averging

