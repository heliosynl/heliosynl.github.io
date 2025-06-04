---
title: "hBN / hBN-graphene phonon polariton"
date: 2025-03-25
excerpt: ''
type: record
tags:
  - record
---

Content
=====
{:.no_toc}

* toc
{:toc}

NMater2020_Direct observation of highly confined phonon polaritons in suspended monolayer hexagonal boron nitride
======

excite hyperbolic phonon polariton in 2d material
- **momentum compensation** above 10^6 cm^-1
  - s-SNOM widely used for 2d polariton probing
    - high resolution imaging
    - momentum compensation typically reaches ~10^5 cm^-1
    - determined by tip size
  - need narrow frequency window

fast electrons can transfer much larger momentum than photons
- EELS
  - high spatial and energy resolution
    - lattice vibrations
    - interband transitions
    - interactions mediated by large-momenta exchanges
      - polariton-induced shift of resonance peak
  - limited by energy resolution for narrow phonon polariton dispersion

hBN flakes STEM-EELS spectra:
- aloof configuration
  - in vacuum
  - 10 nm away from hBN edge
  - one peak at 173 meV
    - consistent with previous work
- bulk geometry
  - inside the flake
  - 20 nm away from hBN edge
  - three peaks, 173 182 196 meV

FEM reproduce EELS spectra of hBN flakes (e beam move from edge to inside)
- 196 meV, right peak
  - between
    - surface optical phonon SO 195 meV
    - LO phonon 200 meV
  - considering zero-loss peak ?
    - gaussian convolution FWHM 7.5 meV
  - 200 meV redshift to 196 meV, LO phonon
  - evenly distributed
    - characteristic of LO phonon
  - SO phonon localized at edge
    - not observed in exp
    - strong localization at boundary
    - imperfection in edge
- 182 meV, central peak
  - shift from 195 meV to 183 meV
  - characteristic of phonon polariton
  - excited polaritons propagete to edge, then are reflected by edge
    - then interfere with the excited polariton
    - interference max:
      - $2q\vert d \vert + \phi_{refl} = 2\pi$
        - $ \phi_{refl} $ is phase change by reflection
        - use $ \phi_{refl} = \frac{\pi}{2} $ here
    - by this relation, extract energy loss spectrum in **momentum space** by spectrum in **distance** space by changing $d$
  - FEM assigned to symmetric surface phonon polariton SM0-S mode
  - originates in the constructive interference of HPhPs reflected by the edge, followed the $2q \vert d \vert + \phi_{refl} = 2\pi$ law
    - frequency (energy loss) more stable when far enough away from the edge (large d)
- 173 meV, left peak
  - close to TO phonon but not TO
    - TO cannot be electrically exicted
  - FEM assigned to SM0-S mode, same to central peak
    - frequency difference due to wave vectors
    - much lower and unchangeable q with position
    - arises due to the excitation of HPhPs propagating along the direction perpendicular to the e beam line scan
    - convolution of several peaks
      - blue shift

FEM reproduce EELS spectra of monolayer hBN
- thickness pick 0.34 nm
- LO TO are degenerated into one point
- only one peak with increasing scanning distance to the edge
  - HPhP modes
  - actually the combination of two peaks, low-q and high-q HPhPs
    - can see two peaks but very close to each other in simulation without zero-loss peak (Gaussian smearing)
    - after smearing they get too close so cant regonize
  - low-q HPhP
    - similar to left peak in flakes
    - doesnt change with scanning distance
    - SM0 mode
  - high-q HPhP
    - similar to central peak in flakes
    - constructive interference, incident and edge-reflected HPhP
      - change with d
      - approach to steady value with increasing d, reflection is ignored with large d