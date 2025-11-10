---
title: "Quantum Mechanics Notes"
date: 2024-12-18
excerpt: 'Some notes for Ab Initio Calculation/ Quantum Mechanics'
type: notes
tags:
  - Quantum Mechanics
  - notes
---

Content
=====
{:.no_toc}

* toc
{:toc}

# Constant
```python
# Energy
# To Ry
ConvHa2Ry=2
ConvJ2Ry=4.587424e+17
ConveV2Ry=7.349862e-02
ConvK2Ry=6.333624e-06
ConvGHz2Ry=3.039660e-07

Convforceau2eVAng=25.710907566423526 # Ry/Bohr to eV/Ang
ConvBohr2Angstr=0.52918 # Bohr same to a.u.

Avogadro=6.02214076e23
pi=np.pi
kB=1.380649e-23 #J K^-1
h=6.62607015e-34 #J s
hbar=h/(2*pi)
epsilon0 = 8.854187812813e-12 #C^2 m^-2 N^-1
me = 9.1093837e-31 #kg
charge=1.602176e-19 #C
c=299792458 #m/s
ccm=c*1e3 #cm/s
```
- vertical: original unit
- horizontal: target unit
 
|    | Ha | J | eV | Ry | K (Temp) | GHz | cm-1|
| ----|----|---|---|---|------|---|---|
| Ha | 1  | 4.359745e-18| 27.211396132 | 2 | 3.157750e+05 | 6.579684e+06|2.194746e+05|
|J|2.293712e+17|1|6.241496e+18|4.587424e+17|7.242969e+22|1.509190e+24|5.034117e+22|
|eV|3.674931e-02|1.602176e-19|1|7.349862e-02|1.160451e+04|2.417988e+05|8.065541e+03|
|Ry|0.5|2.179873e-18|13.60570|1|1.578875e+05|3.289842e+06|1.097373e+05|
|K (Temp)|3.166812e-06|1.380649e-23|8.617337e-05|6.333624e-06|1|2.083662e+01|6.950348e-01|
|GHz|1.519830e-07|6.626070e-25|4.135669e-06|3.039660e-07|4.799243e-02|1|3.335641e-02|
|cm-1|4.556336e-06|1.986446e-23|1.239842e-04|9.112672e-06|1.438777|29.979246|1|

# Optics
- Relative permittivity, dielectric function$$\varepsilon(\omega)=1+\chi(\omega)$$
- Refractive index$$n(\omega)=\sqrt{\varepsilon(\omega)}$$
  - Real part refractive index $$n=\sqrt{\frac{\sqrt{\varepsilon_r^2+\varepsilon_i^2}+\varepsilon_r}{2}}$$
  - Imag part extinction coefficient $$\kappa=\sqrt{\frac{\sqrt{\varepsilon_r^2+\varepsilon_i^2}-\varepsilon_r}{2}}$$
  - Dielectric function in $$\varepsilon_r=n_r^2-n_i^2$$, $$\varepsilon_i=2n_rn_i$$
- Optical absorption coefficient $$\alpha(\omega)=\frac{2\omega}{c}\kappa=\frac{2\omega}{c}n_i$$
- Reflectivity $$R=\frac{(1-n)^2+\kappa^2}{(1+n)^2+\kappa^2}=\frac{(1-n)^2+n_i^2}{(1+n)^2+n_i^2}$$
- Optical conductivity $$\sigma(\omega)=-i\omega\chi(\omega)$$
  - definition $$\vec J(\omega)=\sigma(\omega)\vec E(\omega)$$
  - $$\vec D(\omega)=\varepsilon(\omega)\vec E(\omega)$$
  - $$\varepsilon(\omega)=\varepsilon_0+\frac{i\sigma(\omega)}{\omega}=\varepsilon_0(1+\chi(\omega))$$

# Magnetics
- Macroscopic magnetic moment $$m:\rm A\cdot m^2$$
- $$1 \rm A\cdot m^2=1000 \rm emu (erg/G)$$
- Bohr magneton  $$\mu_B=9.274×10^{-24} \rm A\cdot m^2$$
- Magnetization is defined as net magnetic moment in an unit volume $$M=\frac{m}{V}: \rm \frac{A\cdot m^2}{kg} ; \frac{A\cdot m^2}{mol}$$
- $$1 \rm A\cdot m^2/kg=1 \rm emu/g$$
- $$1 \rm emu/mol=\frac{10^{−3} μ_B}{9.274×10^{−24}\times6.023\times10^{23} f.u.}=\frac{1}{5585} μ_B/f.u.$$
- Where $$f.u.$$ refers to formula unit 

# charged defect formation energy
[3Dreference](https://www.pwmat.com/modulefiles/pwmat-resource/module-download7/pdf/Charged%20defect%20calculation-module.pdf)

[2Dreference](https://www.pwmat.com/modulefiles/pwmat-resource/module-download7/pdf/guide_defect_level_20240709.pdf)