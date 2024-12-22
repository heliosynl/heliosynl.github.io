---
title: 'QE PWscf Band Structures'
date: 2024-12-21
excerpt: 'Quantum Espresso PWscf Band Structure Calculation'
type: notes
tags:
  - Ab Initio
  - Quantum Espresso
  - PWscf
  - notes
---
Example: 4H-SiC crystal
<br/><img src='/images/notes/2024-12-21-QE-PWscf-BandStructure/4H-SiCmodel.png' width="400">

# 0. structural optimization, kpt convergence, ecut convergence, smearing convergence
**Do before any calculation**
# 1. scf
Dense enough K pt mesh

```
&CONTROL
  title = '4H-SiC'
  prefix = '4HSiC'
  outdir = './calout'
  pseudo_dir = '/home/yongnanli08/Desktop/4hsic/PP'
  calculation = 'scf'
  nstep = 1000
  iprint = 1                ! write band information each iprint step
  tprnfor = .true.          ! calculation of force
  tstress = .true.
  restart_mode = 'from_scratch'
  verbosity = 'high'
  forc_conv_thr = 1e-5      ! no need if not relax vc-relax
  etot_conv_thr = 1e-6      ! no need if not relax vc-relax
/
 
&SYSTEM
  nat= 8
  ntyp= 2
  ibrav= 0
  ecutwfc = 90.00
  nosym = .true.            ! no need, use for low-symmetric system (low-dimensional, etc)
  force_symmorphic = .true. ! no need, force the symmetry group to be symmorphic, for yambo init
  ! =========== Smearing ===============
  occupations = 'smearing'
  smearing = 'mp'
  degauss = 1e-3
/
 
&ELECTRONS
  electron_maxstep = 500
  mixing_mode = 'plain'
  mixing_beta = 0.4
  mixing_ndim = 12
  conv_thr =  1.0d-11
  diagonalization = 'david'
  diago_thr_init = 5e-6     ! for charge density, 1e-5, can reduce if not converged
/
 
&IONS
  ion_dynamics = 'bfgs'     ! for structural optimization, relax & vc-relax
/
 
&CELL
  cell_dynamics = 'bfgs'    ! for structural optimization, relax & vc-relax
/
 
ATOMIC_SPECIES
Si  28.085  Si.pbe-n-rrkjus_psl.1.0.0.UPF
C   12.011  C.pbe-n-kjpaw_psl.1.0.0.UPF
 
CELL_PARAMETERS angstrom
   3.099315860  -0.000000000   0.000000000
  -1.549657930   2.684086271   0.000000000
   0.000000000   0.000000000  10.114801588

ATOMIC_POSITIONS angstrom
Si            1.5496594817        0.8946945267        9.4877890025
Si           -0.0000015518        1.7893917439        4.4303882085
Si            0.0000000000       -0.0000000000        6.9598048955
Si            0.0000000000        0.0000000000        1.9024041015
C             1.5496594817        0.8946945267        7.5821765481
C            -0.0000015518        1.7893917439        2.5247757541
C             0.0000000000        0.0000000000        5.0603888110
C             0.0000000000       -0.0000000000        0.0029880170
 
K_POINTS automatic
8 8 8  0 0 0

```

# 2. nscf
actually **no need** (bands calculation is also nscf), the charge density has been determined in scf
- `calculation = 'scf'` to `calculation = 'nscf'`
- k pt `8 8 8` to `16 16 16`

# 3. use `calculation = 'bands'`

```
K_POINTS crystal_b
4 ! num_of_high_symmetry_points
0.0000000000	0.0000000000	0.0000000000 30 ! Gamma
0.5000000000	0.0000000000	0.0000000000 20 ! M
0.3333333333	0.3333333333	0.0000000000 30 ! K
0.0000000000	0.0000000000	0.0000000000 20 ! Gamma
```
The numbers following the coordinates are, the point interval between this high symm. point to the next one while doing interpolating. High symmetry path can check by upload **bulk** pwscf input file to [seekpath](https://www.materialscloud.org/work/tools/seekpath). High symmetry point coordinates are in **reduced form**, in reduced first Brillouin zone!

Can also use Python script [KptPath](/codes/kptpath/) with `K_POINTS crystal`, same function with `K_POINTS crystal_b`.

# 4. bands.x post-processing
## bands.x

```
&BANDS
  prefix = ''
  outdir = ''
  filband = '_bands.dat'
/

```
will get _bands.dat, _bands.dat.gnu, _bands.dat.rap

# 5. plotbands.x

don't trust its output of `high-symmetry point: `, it is in **cartesian coordinates**, but we want high symm. point in **crystal/reduced coordinates**!

```
> plotband.x
     Input file > 4HSiCslabC_bands.dat
Reading   24 bands at     71 k-points
Range:  -13.9960    7.1910eV  Emin, Emax, [firstk, lastk] > -6,8
high-symmetry point:  0.0000 0.0000 0.0000   x coordinate   0.0000
high-symmetry point:  0.5000 0.2887 0.0000   x coordinate   0.5774
high-symmetry point:  0.3333 0.5774 0.0000   x coordinate   0.9107
high-symmetry point:  0.0000 0.0000 0.0000   x coordinate   1.5773
output file (gnuplot/xmgr) > gnuplot
bands in gnuplot/xmgr format written to file gnuplot

output file (ps) > (press enter)
stopping ...
```
generate several gnuplot files, splited by high-symmetry points

# 6. gnuplot
```
gnuplot -p -e "plot 'gnuplot.1.1' w l, 'gnuplot.2.1' w l, 'gnuplot.3.1' w l"
```

![BulkBand](/images/notes/2024-12-21-QE-PWscf-BandStructure/4H-SiCbulk.png)
