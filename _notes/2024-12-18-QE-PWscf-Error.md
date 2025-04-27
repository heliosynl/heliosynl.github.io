---
title: 'QE PWscf Error shooting'
date: 2024-12-18
excerpt: 'Error shooting for Quantum Epresso PWscf, collecting from internet and by my experience'
type: notes
tags:
  - Ab Initio
  - Quantum Espresso
  - PWscf
  - notes
---

Content
=====
{:.no_toc}

* toc
{:toc}

## SCF convergence problems
### parameters recommendations
#### CONTROL namecard
- `nstep = 1000`
- `forc_conv_thr = 1e-5` in Ry/Bohr, sometimes can not converge, maybe a little bit too high for some cases, equivalent to 2.57e-4 eV/Angstr
- `etot_conv_thr = 1e-6` always good if no SCF convergence problems
- `dipfield = .true., tefield = .true.` for using dipole correction for polar slab system with vacuum layer
#### SYSTEM namecard
- `ecutwfc` see recommended value from each pseudopotential files
$$\Delta E < 2\times10^{-5} \rm Ry/atom$$
- `ecutrho` can be 8-10*`ecutwfc` for Ultrasoft, usually 4*`ecutwfc` (default) is ok
- `nosym = .true., force_symmorphic = .true.` for defected, slab, not bulk system, the latter is for yambo
- `occupations = 'smearing', smearing = 'mp', degauss = 1e-3` about 300 K, for conductor should do convergence test of `degauss`, for insulator can choose `occupations = 'fixed'` (also need for Berry phase calculation)
- `degauss` smearing contribution as small as possible
$$<1\times10^{-4} \rm Ry/atom$$
- `edir = 3, eamp = 0.0, emaxpos = 0.9, eopreg = 0.02` for vacuum layer at z-direction, slab located at the middle of unit cell, `emap` means balanced charged sides of slab, `emaxpos` refers to the location where to appear correction, `eopreg` refers to the length of correction
- `edir = 3, eamp = 0.0, emaxpos = 0.8, eopreg = 0.02` for slab located at bottom of unit cell, check carefully if `emaxpos` go across the slab model
#### ELECTRONS namecard
- `electron_maxstep = 500` good
- `mixing_mode = 'plain'` for common cases, `mixing_mode = 'local-TF'` for reduced-dimensional cases
- `mixing_beta = 0.6` for common cases, `mixing_beta = 0.3` for 2D cases
- `mixing_ndim` = 12 for **local PC**, `mixing_ndim = 16` for **HPC** first try
- `conv_thr = 1e-11` is ok for **scf** and **nscf**, `conv_thr = 1e-9` for **relax** and **vc-relax**
- `diagonalization = 'david'` for common cases, `diagonalization = 'cg'` much slower but robust, can try if not converged.

During nscf (as well as bands) KS eigenvalues are diagonal to full accuracy (diago_full_acc=.true. by default), at variance with scf calculations, where accuracy is lowered for empty states (not relevant to compute the density not the total energy).
While one could set diago_full_acc=.true. in scf runs, it is anyway highly recommended to run a second nscf calculation to perform BZ refinements or increase the number of state for plotting or inspection.

#### K_POINTS namecard
``8 8 2  0 0 0`` no grid shift if doing yambo

### too many eigenvalues not converged found in the last iteration steps
- Changing pseudopotential types: USPP, NCPP, PAW PP
- Increase ecutwfc with ecutrho=4*ecutwfc (for ONCVP, 8-10 for USPP)
- Decreasing conv_thr parameter (scf 1e-11, relax 1e-9)
- Decreasing mixing_beta (0.1-0.3 is ok for slab)
- Changing ion_dynamics and cell_dynamics (usually bfgs)
- Decreasing k meshing

### can not reach convergence till all scf steps
- reduce `mixing_beta` default 0.7, can be 0.1-0.3 for slab model (<0.05 for very long slab). It reudces the mixing ratio of charge density from the previous iterative steps
- increase `mixing_ndim` to 12 (for local PC) or higher (16 for HPC is totally ok and can be more larger like 24). Determine how many iterative steps are considered for charge density mixing of `mixing_beta`
- use `mixing_mode` of `local-TF` for slab model
- change 

### too many processors
No share memory parallel (OpenMP) in my computer
```bash
OMP_NUM_THREADS=1
```
in batch file (or ~/.bashrc file for local computer)

### fatal error in internal_gather: message truncated, error stack:
Similar things:
- Caught signal 11 (Segmentation fault: address not mapped to object at address (nil))
- message...

Problems relate to MPI, we call mpi out of memory, may be cause by the long address and inter-overlapping

can try:
- use fewer cores (just test in local PC first and see whether it can start calculate)
- incresae the allocation of memory (in slurm, that is `#SBATCH --mem=600G`), useful for very large system

## Geometry
Provided known space_group, don’t use ibrav
ATOMIC_POSITION crystal_sg
nat is supposed to accord to inequivalent atoms, which is, irreducible form of atoms in primitive cell
Irreducible form of atoms can be obtained from VESTA by loading primitive cell file

### If band gap exists in ground state calculation: **need test and example**
Use ``occupation = 'fixed'``, ``tot_magnetization`` with accordance to previous SCF results, ``nbnd`` with accordance to number of Kohn-Sham states in previous SCF results. The use of ``startingpot`` and ``startingwfc`` (in ``&Electron``) is recommended to reduce CPU time and avoid from divergence