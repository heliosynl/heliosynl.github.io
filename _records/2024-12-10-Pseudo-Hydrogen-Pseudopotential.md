---
title: "Pseudo-Hydrogen Pseudopotential Generation for "
date: 2199-12-18
type: notes
tags:
  - ab initio
  - quantum espresso
  - notes
---
For slab model, we can regard the model as the sliced bulk material, in which the bonds between atoms are cut, forming termination layers. If we are considering the **surface states** or **superficial properties** of **real** materials, the unstaturated bonds at the surfaces act inevitable roles. In DFT atomistic model, unless the model is large enough, the bottom atomic layer usually interferes the charge distribution and charge transfer of the upper-most atomic layer - the surface layer we are interested in, by the finite number of atomic layers. To avoid this influence, a method called **Pseudo-Hydrogen** is well-adopted, to saturate the additional bonds located at the bottom atomic layer. By doing so, we can prevent the artificial and unphysical charge transfer from the bottom layer to the upper-most layer, allowing the prediction of **real** surface states distribution at the surfaces.

The implementation of the pseudo-hydrogen method requires basic understading of the bonding types of the target slab material in bulk state. In particular, the covalent bond in ZnO, where Zn2+ holds 6 outter-most electrons and O2- holds 2 outter-most electrons. The covalent bond formed in bulk ZnO crystal reflects a 3:1 ratio of contribution of a full 