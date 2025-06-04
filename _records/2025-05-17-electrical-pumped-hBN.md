---
title: "Electrically pumped h-BN single-photon emission in van der Waals heterostructure"
date: 2025-05-17
excerpt: 'test'
type: record
tags:
  - record
---

Content
=====
{:.no_toc}

* toc
{:toc}

# Introduction

p1
=====
1. defects in quantum technologies 
2. defects in 2d materials, quantum circuitries
3. example of defects in 2d materials (hBN), SPE, quantum communication
4. challenges, optical pumping, difficulties in manipulation in integrated structures

p2
=====
1. advantages in electrical excitation
2. advatnages when incorporating with 2d materials (van der waals materials)
3. more details of electrical excitation, mechanisms of charge carriers injection
4. good but not implemented, emphasizing the innovative points (electrical pumped, hBN, SPEs, isolated defect)

p3
=====
1. devices they proposed, can achieve SPE in hBN, atomically thin
2. brief structure of devices (hetero- van der waals junction, NbSe2/hBN/graphene), electrical pumping
3. some properties, photon emission intensity scales linearly with the applied current, antibunching natures in HBT configuration
4. advantages of heterojunction configuration, enabling stable defect emission, other characterization of photon emission (photon energies, polarization) **but not sure why heterojunction can allow this, very special? hard in other configuration?**
5. brief conclusion, outlook of the electrically pumped hBN SPE, potential applications in compact devices, chip-based quantum information

# Results and dicussion

p1
=====
1. device configuration
2. defect formation in hBN
  - high temperature annealing with O2 gas flow to high purity hBN crystal
  - additional pristine hBN space layer is placed between defective hBN and top NbSe2 as part of sequential transfer of multilayer stacking (**just for stacking? dont know whats for**)
  - details go to SI
3. again, how electrical pumping works for emission

p2
=====
1. chosen of electrode materials in heterostructure, NbSe2 and graphene, asymmetric junction, efficient charge carriers injection
2. minimal overlapping of two electrodes, confining the path of tunneling current flow to go through the defects
3. reducing the number of participating defects in tunneling current flow can stabilize photon emission

p3
=====
1. electroluminescence measurement details, 6.5 K, varying voltage
2. Figure 1b, electrically induced emission spectrum, description of experiments, some devices details (hBN spacer thickness and defective hBN thickness)
3. trend of intensity change with increasing applied voltage
4. CCD image Figure 1c, white light source, identify graphene, NbSe2 by their boundaries, localized EL center (with EL mapping image)

p4
=====
1. more specific comparison of EL spectrum, 0 V and 28 V
2. emission peaks 1.5 2.8 2.9 eV, ZPLs of single defects
3. 2.6 eV is phonon sideband of 2.8 eV, reference longitudinal optical phonon of hBN
4. 1.5 eV free of separate phonon sideband
5. some have sideband some have not, originate from layered structure (vdW interaction?), with reference
6. asymmetric ZPL with higher spectral weight toward low energy side, originated from low-energy acoustic phonon sidebands (i.e. low freq phonon contribution to boardening/sideband) or the voltage induced peak broadening

p5
=====
1. focus more on 1.5 eV ZPL
2. high resolution spectra of 1.5 eV ZPL, showing in Figure 2a 2b, showing threshold voltage 26 V
3. emission intensity and tunneling current as functions of voltage Figure 2c, intensity scale linearly with current, with same threshold voltage
4. above finding suggests tunneling current is induced by defect-mediated charge transport directly contributing to the charge carrier supply at the emitter site (**not very understandable, assuming intensity - current is linearly related?**)
5. linear relation between tunneling current and emission intensity, even for less stable emissters (intermittent blinking), positive correlation between current and intensity still existed, indicating emissions are driven by current flow
6. emphasize again the correlation between current and emission intensity is a strong piece of evidence of charge transport through a single defect, which is a distinct behavior enabled by van der Waals device

p6
=====
1. looking deeper into the voltage dependent emission, a Stark shift is foudn in Figure 2a, representing **out-of plane dipole**
2. width increases with voltage in Figure S4
3. peak broadening is explained by the increase of injection current, enhancing the charge carriers in the vicinity of defect site, field fluctuation by surrouding mobile charges
4. field fluctuation coupled to the increase dipole mement with voltage, resulting in the inhomogeneous broadening of emission peaks
5. Figure S4, inhomogenous broadening is more pronounced toward the low energy side as voltage increases, unlink optically excited hBN
6. however the minimal linewidth increasement is only 2 meV by measurement, still comparable to most optically excited hBN and electricaly excited emitters in other solid state systems

p7
=====
1. single photon emission properties, confirmed by second order correlation function measurement
2. Figure 2d, g2tau
3. g2tau data description, g2(0) = 0.25 +- 0.21 quantum nature
4. width of tip 18.2 +- 7.2 ns, longer than typical lifetimes from optically excited hBN (a few ns)
5. longer lifetime comes from the distinctive transition process associated to electrical excitation
6. current injuection supplies carriers to defect site across the bandgap, highly probable include charge-trapping level during the excitation process, thus slower transition process
7. more details of transition mechanism in SI

p8
=====
1. g2tau photon count rate ~700 cps with current level 6 nA
2. total measurement time about 25 h gives the conincidence count event number of 75 at a large time delay
3. photon emission count rate is smaller than other electrically excited SPE in **bulk** host materials but comparable to other **ultrathin** crystals
4. assume high threshold voltage prevent the increase of the applied voltage, resulting in a moderate injuection current
5. but some fabricated devices may have lower threshold, expect preparing **cleaner interfaces**, improving **contact quality** can decrease threshold, enhance the emitter intensity and scalability 

p9
=====
1. check the dipole axis direction of emitter by the polarization-resolved measurement in Figure 2e
2. fitting the polar plot of the angle-resolved emission intensity with $ I(\theta) = A cos^2(\theta-\theta_0)+B $, $\theta$ is the polarization angle of the emitted light measured relative to the high symmetry axis of hBN crystal, find $\theta_0 = 60\degree$

p10
=====
1. emission wavelength and intensity showed good instability as a funciton of time, Figure 2f
2. emission intensity, generally persistent value, a few intermittent brightening
3. another emitter better stability in terms of intensity, Figure S3, lower voltage (23 V)
4. analyzing the blinking statistics by recording the emission on and off events, to know the intermittent brightening, Figure S6
5. from above, extracted the effect of surrounding itinerant mobile charges is a dominant origin of the intensity fluctuation

p11
=====
1. SI section 6, summarize the number of emitters in 4 devices
2. more than 30 emitters in device 1 through electrical pumping, good stability.
3. other than emitter in Figure 1, some emitters were **created** with applied voltage above 60 V on the same device, Figure S7
4. several reasons of such high voltage created defect levels
5. existing defect levels may changed by the voltage-induced charge injection, or new sites be created by breaking B-N bonding
6. the possible mechanisms of defects creation under high voltage suggests, local electrical pulse at the device level could be applied to controllably activate emission centers for defect creations

p12
=====
1. emission energy with positive and negative voltage, to understand the charge supply mechanism of the heterostructure, Figure 3
2. two characteristics
3. number of emitters far exceeds at positive than negative bias
4. high photon energies, most emitters are observed under the application of positive voltages with only a few exception

p13
=====
1. observation of different voltage bias align with the band diagram
2. work function of graphene 4.5 eV and NbSe2 5.9 eV, without bias, the heterostructure creates a built-in tilting in hBN, Fermi level of NbSe2 becomes closer to the hBN VBM
3. applying finite volatge, current flow supplies electrons and holes into the defect sites, photon emission
4. the current flow luminescence processs occurs more efficiently under a positive bias, because NbSe2 is a hole metal, preferentially provides hole carriers for the tunneling current
5. holes from NbSe2 and electrons from graphene allow stable generation of photons
6. negative voltage, electron are less supplied, more pronounced for emitters with higher transition energies

p14
=====
1. with information of polarization axis, wavelength, can categorize emitters into **three** groups, could have **distinct** cyrstallographic structures, Figure 4
2. long wavelength group with energy 1.4-1.7 eV, middle wavelength group with energy 1.9-2.4 eV, short wavelength group with energy 2.4-3.0 eV
3. different groups show characteristic photon energy, shape of phonon sideband, polarization dependence, implying different origins

p15
=====
1. group 1 small phonon sidebands, randomized distribution of polarization axis
2. oxygen related defect, from emission energy range and shape of spectrum
3. the abundance of group 1 emitters may result from the oxygen-flow annealing during fabrication
4. using argon-annealing, strikingly constrasting emitter distribution is found in Figure S8
5. highlights the accessibility of EL probe oxygen-related defectst in hBN
6. group 3 phonon sidebands 160 meV apart from ZPL, linear polarization axes generally separated by a 60deg interval
7. polarization axis is particularly more concentrated at 120deg, could be result of the **uniaxial strain** frequently foudn in layered materials
8. polarization dependence agress with the recently reported emitteres induced by e-beam irradiation, carbon ion implantation
9. suggest group 3 may originiate from carbon-related color center
10. group 2 wide range of variation in both spectral shape and polarization distribution
11. short outlook, need more research to understand

# Conclusion
1. demonstrate all electrical generation of SPE in hBN, van der Waals integrated devices scheme
2. combination of graphene and NbSe2, asymmetric deivce structure, stable generation of photon emission in a wide range of spectral windows, allowing studies on various types of emitters
3. aniticipate, expand research on 2d materials in **heterostructure** involving hBN defects, will promote funtionality and applicability of van der Waals quantum optoelectronics
4. outlook integrable single photon sources in ultrathin materials, electrical excitation capabilities, may achieve **electrically driven** quantum communication, spin defect operations