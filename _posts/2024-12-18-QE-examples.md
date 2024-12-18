---
title: 'QE PWscf examples'
date: 2199-12-18
type: notes
tags:
  - ab initio
  - quantum espresso
  - PWscf
  - notes
---

# pw.x 
```
&CONTROL
  title = ' '
  prefix = ' '
  outdir = './calout'
  pseudo_dir = '/home/yongnanli08/PP'
  calculation = 'scf'
  nstep = 1000 
  iprint = 1 ! write band information each iprint step
  tprnfor = .true. ! calculation of force
  tstress = .true.
  restart_mode = 'from_scratch'
  verbosity = 'high'
  disk_io = 'high'
  forc_conv_thr = 1e-5
  etot_conv_thr = 1e-6
  ! =========== Berry phase calculation ===============
  ! lelfield = .true.
  ! nberrycyc = 1
  ! =========== Dipole correction ===============
  ! dipfield = .true.
  ! tefield = .true.
/
 
&SYSTEM
  nat= 
  ntyp= 
  ibrav= 0
  ecutwfc= 40 ! in Ry, 40 Ry = 520 eV
  occupations = 'smearing'
  smearing = 'mp'
  degauss = 1e-3 ! about 300 K
  nosym = .true.
  force_symmorphic = .true. ! force the symmetry group to be symmorphic, for yambo
  ! =========== DFT D3 2009 =============== 
  vdw_corr = 'DFT-D3'
  dftd3_version = 6
  ! =========== Dipole correction ===============
  edir = 3 ! z-axis
  eamp = 0.0
  emaxpos = 0.82
  eopreg = 0.02
/
 
&ELECTRONS
  electron_maxstep = 500
  mixing_mode = 'local-TF' ! Plain TF local-TF
  mixing_beta = 0.2 ! Reduce if slab model not converged
  mixing_ndim = 16 ! Increase if large of RAM
  conv_thr =  1e-11 ! can be 1e-9 for relaxation
  diagonalization = 'david' ! david cg ppcg
  startingwfc='random'
  diago_thr_init = 5e-6 ! for charge density, 1e-5, can reduce if not converged
  ! diago_full_acc = .true. ! all empty states are diagonalized at the same level of accuracy, need in nscf
/
 
&IONS
  ion_dynamics = 'bfgs'
/
 
&CELL
  cell_dynamics = 'bfgs'
/
 
ATOMIC_SPECIES
C   12.011  C.ONCVP.PBE.stringent.upf
 
CELL_PARAMETERS angstrom
      6.19864000        0.00000000        0.00000000
     -3.09931600        5.36817278        0.00000000
      0.00000000        0.00000000       100
 
ATOMIC_POSITIONS angstrom
H         0.00000000        0.00000000        0.00299400
 
K_POINTS automatic
2 2 1  1 1 0

```

## band structure calculation
1. scf
2. nscf
3. use `calculation = 'bands'`
```
K_POINTS crystal_b
num_of_high_symmetry_points
0.0000000000	0.0000000000	0.0000000000 30 ! Gamma
0.5000000000	0.0000000000	0.0000000000 20 ! M
0.3333333333	0.3333333333	0.0000000000 20 ! K
0.0000000000	0.0000000000	0.0000000000 30 ! Gamma
```
high symmetry path can check by upload **bulk** pwscf input file to [seekpath](https://www.materialscloud.org/work/tools/seekpath)

4. bands.x post-processing
5. plotbands.x
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
6. gnuplot
```
> gnuplot -p -e "plot 'gnuplot.1.1' w l, 'gnuplot.2.1' w l, 'gnuplot.3.1' w l"
```
# bands.x
```
&BANDS
  prefix = ''
  outdir = ''
  filband = '_bands.dat'
/

```
will get _bands.dat, _bands.dat.gnu, _bands.dat.rap

# hp.x
```
&inputhp
  prefix = ''
  outdir = ''
  nq1 = 2
  nq2 = 2
  nq3 = 2
  conv_thr_chi = 1.0d-6
  iverbosity = 2
/

```

# dos.x
```
&dos
  prefix  = ''
  outdir  = ''
  Emin = 
  Emax = 
  DeltaE = 
  fildos = ''
/

```

# projwfc.x
```
&projwfc
  prefix  = ''
  outdir  = ''
  Emin = 
  Emax = 
  DeltaE = 
  filpdos = ''
  plotboxes = .true.
/

```
L=1:
Ordering: p_z  p_x  p_y
L=2:
Ordering: d_(z^2 )  d_xz  d_zy  d_(x^2−y^2 )  d_xy

# pp.x
```
&inputpp
  prefix  = ' '
  outdir  = './calout'
  filplot = 'qeppoutput' ! file saving charge density in qe format
  plot_num=  ! Differential charge density 9, electrostatic potential (V_bare + V_H) 11, ELF 8
 /

&plot
  nfile = 1
  iflag = 3 ! 3D ploting
  output_format = 6 ! Can be read by VESTA
  fileout = 'charge.prefix.cube' ! Can be read by VESTA
  e1(1)=1.0,e1(2)=0.0,e1(3)=0.0,
  e2(1)=0.0,e2(2)=1.0,e2(3)=0.0,
  e3(1)=0.0,e3(2)=0.0,e3(3)=1.0,
  x0(1)=1.0,x0(2)=0.0,x0(3)=0.0,
  nx=101,ny=101,nz=2001
  ! e1 e2 e3 plotting parallelepiped vectors
  ! x0 origin of the parallelepiped
  ! nx ny nz number of points in the parallelepiped
/

```