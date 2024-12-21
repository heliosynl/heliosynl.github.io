---
title: 'QE PWscf Input Examples'
date: 2024-12-18
excerpt: 'Example input files for Quantum Espresso PWscf and some extensions.'
type: notes
tags:
  - Ab Initio
  - Quantum Espresso
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
  iprint = 1                ! write band information each iprint step
  tprnfor = .true.          ! calculation of force
  tstress = .true.          ! calculation of stress
  restart_mode = 'from_scratch'
  verbosity = 'high'
  disk_io = 'high'
  forc_conv_thr = 1e-5      ! no need if not relax vc-relax
  etot_conv_thr = 1e-6      ! no need if not relax vc-relax
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
  nosym = .true.            ! no need, use for low-symmetric system (low-dimensional, etc)
  force_symmorphic = .true. ! no need, force the symmetry group to be symmorphic, for yambo init
  ! =========== DFT D3 2009 =============== 
  ! vdw_corr = 'DFT-D3'
  ! dftd3_version = 6
  ! =========== Assume isolation ===============
  ! assume_isolated = 'esm' ! 2D, no need esm_bc
  ! esm_bc = 'bc1'
  ! =========== Dipole correction ===============
  ! edir = 3 ! z-axis
  ! eamp = 0.0
  ! emaxpos = 0.5
  ! eopreg = 0.02
/
 
&ELECTRONS
  electron_maxstep = 500
  mixing_mode = 'local-TF' ! Plain TF local-TF
  mixing_beta = 0.2 ! Reduce if slab model not converged
  mixing_ndim = 16 ! Increase if large of RAM
  conv_thr =  1e-11 ! can be 1e-9 for relaxation
  diagonalization = 'david' ! david cg ppcg
  startingwfc='random'
  diago_thr_init = 5e-6     ! for charge density, 1e-5, can reduce if not converged
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
Ordering: d_(z^2 )  d_xz  d_zy  d_(x^2-y^2 )  d_xy

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
