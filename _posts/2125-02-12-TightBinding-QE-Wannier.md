---
title: "Wannier function calculation with Wannier90 and QE"
date: 2125-02-12
excerpt: 'From QE Bloch states to specific spatial localized Wannier functions'
type: blog
tags:
  - Tight-binding
  - QE
  - Wannier
  - blog
---

Content
=====
{:.no_toc}

* toc
{:toc}

Theory of tight-binding model
=====
**Updating**

Take **graphene** as example, do wannier calculation first
# 0. structural optimization, kpt convergence, ecut convergence, smearing convergence
**Do before any calculation**
# 1. scf
Dense enough K pt mesh

```
&CONTROL
  title = 'mono layer graphene'
  prefix = 'mono'
  outdir = './calout'
  ! pseudo_dir = '/lustre1/u/ynl08/PP'
  pseudo_dir = '/home/yongnanli08/PP'
  ! pseudo_dir = '/GLOBALFS/yt_hku_ygli_1/BLG/PP'
  calculation = 'scf'
  nstep = 1000
  iprint = 1 ! write band information each iprint step
  tprnfor = .true. ! calculation of force
  tstress = .true.
  restart_mode = 'from_scratch'
  verbosity = 'high'
  forc_conv_thr = 1e-5
  etot_conv_thr = 1e-6
/
 
&SYSTEM
  nat= 2
  ntyp= 1
  ibrav= 0
  ecutwfc= 80
  occupations = 'smearing'
  smearing = 'mp'
  degauss = 1e-3
  ! =========== DFT D3 2009 =============== 
  vdw_corr = 'DFT-D3'
  dftd3_version = 6
  assume_isolated = '2D'
  ! =========== For yambo =============== 
  force_symmorphic = .true. ! force the symmetry group to be symmorphic
  nosym = .true.
/
 
&ELECTRONS
  electron_maxstep = 500
  mixing_mode = 'local-TF'
  mixing_beta = 0.4
  mixing_ndim = 16
  conv_thr =  1.0d-11
  diagonalization = 'david'
  diago_thr_init = 5e-6 ! for charge density, 1e-5 
  ! diago_full_acc = .true. ! all empty states are diagonalized at the same level of accuracy 
/
 
&IONS
  ion_dynamics = 'bfgs'
/
 
&CELL
    cell_dynamics   = 'bfgs'
/
 
ATOMIC_SPECIES
C    12.011  C.pbe-n-kjpaw_psl.1.0.0.UPF

CELL_PARAMETERS (angstrom)
   2.466116442   0.000000001  -0.000000000
  -1.233058220   2.135719455   0.000000000
  -0.000000004  -0.000000001  23.00

ATOMIC_POSITIONS (angstrom)
C             0.0000000000        0.0000000000        0.0000000000
C            -0.0000000028        1.4238129172        0.0000000000

K_POINTS automatic
30 30 1  0 0 0

```

# 2. nscf
- `calculation = 'scf'` to `calculation = 'nscf'`
- `K_POINTS automatic` to `K_POINTS crystal`
  - use [kpointgen]() to generate **uniform** k point mesh
  - also `30 30 1` here but uniform mesh (try less for testing)

# 3. Wannier90 pre-processing
wannier90.x input file

`wannier90.x -pp seedname`

# 4. PWSCF to Wannier90
`mpirun pw2wannier90.x < prefix.pw2wan.in > pw2wan.prefix.out`

# 5. Wannier90
`wannier90.x seedname`