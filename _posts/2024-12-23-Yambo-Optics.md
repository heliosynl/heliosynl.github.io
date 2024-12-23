---
title: 'Yambo for Linear Optics responses'
date: 2024-12-23
excerpt: 'Yambo linear optics responses calculation'
permalink: /posts/2024/blog1223/
type: blog
tags:
  - Ab Initio
  - Yambo
  - Linear Optics
  - blog
---
Optical responses of materials can be computed based on linear response theory, in which considering the electron density response of system to the external electric field. This is linked to the electric displacement field and the polarization field in Maxwell equations:

$$\vec D(\omega)=\varepsilon_0 \varepsilon_r(\omega) \vec E(\omega)=\varepsilon_0 (1+\chi) \vec E$$

in which $$\varepsilon_r=1+\chi$$ is the **relative** dielectric constant, and $$\chi$$ is the electric susceptibility, defining the polarization field $$\vec P=\chi \vec E$$

For simply, use $$\varepsilon(\omega)=1+\chi(\omega)$$ as relative dielectric function, considering its spectral dispersion.

In short, the (**reversed**) dielectric function is the **response function** of the external field. Or, the electrical susceptibility is response function. The generalized form of the definition of response function $$\chi(t)$$ is

$$F(t)=\int_0^{\infty} \chi(\tau) g(t-\tau) d\tau $$

In electric field expression, it is

$$V_{scattering}(\vec r,t)=V_{ext}(\vec r,t)+V_{ind}(\vec r,t)$$
$$V_{scattering}(\vec r,\omega)=\int d\vec r' \chi_{nn}(\vec r, \vec r', \omega)V_{ext}(\vec r,\omega)$$


For Yambo calculation, a prelinminary SCF (or NSCF) calculation of the electron density distribution is needed. Below takes QE PWscf as example
# 0. scf (or nscf)
go to output file, go `prefix.save` folder, type `p2y` (pwscf to yambo for memorizing)

The following is an example of the band structure calculation for 4H-SiC bulk crystal in 1x1x1 unit cell.

Example: 4H-SiC crystal, typical wide-bandgap semiconductor, usually for high-power electronics, substrate in semiconductor industry.
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

Obviously an indirect band gap is found, between Gamma point as VBM and K point as CBM.
