---
title: "Ab Initio Notes"
date: 2024-12-18
excerpt: 'Some notes for Ab Initio Calculation/ Quantum Mechanics'
type: notes
tags:
  - Ab Initio
  - notes
---
# Constant
```python
# Energy
# To Ry
Conv_Ha2Ry=2
Conv_J2Ry=4.587424e+17
Conv_forceau2eVAng=25.710907566423526 # Ry/Bohr to eV/Ang
Conv_Bohr2Angstr=0.52918 # Bohr same to a.u.

Avogadro=6.02214076e23
pi=np.pi
kB=1.380649e-23 #J K^-1
h=6.62607015e-34 #J s
hbar=h/(2*pi)
epsilon0 = 8.854187812813e-12 #C^2 m^-2 N^-1
me = 9.1093837e-31 #kg
charge=1.60218E-19 #C
c=299792458 #m/s
```

|    | Ha | J | eV | Ry | K (Temp) | GHz |
| ----|----|---|---|---|------|---|
| Ha | 1  | 4.359745e-18| 27.211396132 | 2 | 3.157750e+05 | 6.579684e+06|
|J|2.293712e+17|1|6.241496e+18|4.587424e+17|7.242969e+22|1.509190e+24|
|eV|3.674931e-02|1.602176e-19|1|7.349862e-02|1.160451e+04|2.417988e+05|
|Ry|0.5|2.179873e-18|13.60570|1|1.578875e+05|3.289842e+06|
|K (Temp)|3.166812e-06|1.380649e-23|8.617337e-05|6.333624e-06|1|2.083662e+01|
|GHz|1.519830e-07|6.626070e-25|4.135669e-06|3.039660e-07|4.799243e-02|1|