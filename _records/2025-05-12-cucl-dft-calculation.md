---
title: "record"
date: 2025-05-12
excerpt: 'Yuchen CuCl DFT calculation'
type: record
tags:
  - record
---

Content
=====
{:.no_toc}

* toc
{:toc}

DFT calculation of 6 configuration of Cu-Cl-water molacule
- system energy
  - transition pathway
- further
  - optical absorption? can be use for UV spectrum reasoning

# 2025-05-22
free energy (formation energy?) calculation

single Cu
=====
- /cucl/May23/cu
singlecu2=-401.96197944
singlecu1=-403.07135668

single Cl
=====
- /cucl/May23/cl
singlecl=-34.88951178

H2O
=====
- /cucl/May12/h2o
singleh2o=-44.04153750

# 2025-05-23
drawing atomic model
- color
  - Cu2+
    - #650065
    - #BE63BE
    - #E3BDDC
  - Cu1+
    - #A35331
    - #FFA57F
    - #FF8653 
  - O
    - #7E7E7E
  - H
    - #BFBFBF
  - Cl
    - #1EFFEF
#23b8ae

# 2025-05-25
- **maybe not correct (not pure Cu-Cl complex but with other atoms)**
- Cu(I)Cl2 bond distance (Cu-Cl) = 2.104 A
  - angle=175.9deg
- Cu(I)Cl3 bond distance (Cu-Cl) = 2.165+-(12) A
  - angle=120(+-1.5)
reference: https://www.mdpi.com/2304-6740/13/2/36

- Cu(H2O)6
  - 6 coordinations structure
    - bond distance
      - in xy plane = 1.97A
      - z = 2.38A
    - /May25
      - relaxing
    - reference https://doi.org/10.1016/S0009-2614(00)01110-6
  - 5 coordinations structure
    - /May22/6W5L
      - relaxed scf finished
      - cuh2o6l5=-667.01612658
        - cuh2o6l5-singlecu2-singleh2o*6
          - -0.8049221400000306
    - reference https://pubs.acs.org/doi/abs/10.1021/jp1000804
  - 4 coordinations structures
    - 2 variants
      - 6W4L1
        - /May22/6W4L1/
        - relaxed scf finished
        - cuh2o6l41=-666.99439952
          - cuh2o6l41-singlecu2-singleh2o*6
            - -0.7831950800000413
      - 6W4L2
        - /May22/6W4L2/
        - relaxed scf finished
          - cuh2o6l42=-667.06330550
            - cuh2o6l42-singlecu2-singleh2o*6
              - -0.8521010599999954
    - reference https://pubs.acs.org/doi/abs/10.1021/jp1000804

- CuCl(H2O)5
  - replace one h2o from 6W4L2
  - /May23/5W1Cl
    - relaxed scf finished
      - cuclh2o5=-658.25247725
        - cuclh2o5-singlecu2-singlecl-singleh2o*5
          - -1.1932985299999928
  - reference https://pubs.acs.org/doi/abs/10.1021/jp1000804

- CuCl2(H2O)4
  - replace two h2o form 6W4L1
  - /May23/4W2Cl
    - relased scf finished
      - cucl2h2o4=-649.32743653
        - cucl2h2o4-singlecu2-singlecl*2-singleh2o*4
          - -1.4202835300000345
  - reference https://pubs.acs.org/doi/10.1021/jp909092p


- Cu(I) chloride
  - CuCl
    - without water /May25/0W1Cl+1
      - relaxing
      - scf finished
        - cucl=-438.29948177
          - cucl-singlecu1-singlecl
            - -0.3386133099999924
    - may have 1 water molecule /May25/1W1Cl+1
      - relaxing
      - scf finished
        - cuclh2o=-482.42694170
          - cuclh2o-singlecu1-singlecl-singleh2o
            - -0.42453573999998184
    - reference https://doi.org/10.1016/S0009-2614(00)01110-6
  - CuCl2 -
    - /May23/0W2Cl+1
      - relaxed scf finished
        - cucl2=-473.36700849
          - cucl2-singlecu1-singlecl*2
            - -0.5166282499999824
    - reference https://doi.org/10.1016/S0009-2614(00)01110-6
  - CuCl3 2- at 25 C is found but with **very weak bonded Cl-**, at high Cl- concentration
  - reference: https://doi.org/10.1016/j.gca.2006.09.015
  - https://doi.org/10.1021/acs.analchem.5b00052
    - this paper pointed out, for Cu chloride, whatever valence, coordination number with Cl- increased with increasing Cl- ion concentration in solvation, predicted the existence of Cu(I)Cl3 2- even at low concentration.
    - but my calculation cant predict the structure of Cu(I)Cl3 2-, this paper also not considered the structure but only the reaction
  - https://doi.org/10.1016/j.gca.2012.10.027
    - Fig. 11
      - CuCl2 to CuCl3 at room temperature, log K < 0, not that stable
  - https://doi.org/10.1016/j.gca.2006.09.015
    - Fig .1 from reference
      - CuCl3 dominate only at high Cl concentration, low pH (<9)
- Cl(H2O)6
  - /May25/Cl6W-1/
    - relaxed scf finished
      - clh2o6=-299.28590227
        - clh2o6-singlecl-singleh2o*6
          - -0.14716549000002033

  - reference https://doi.org/10.1039/C3CP50652E
    - chloride ion prefer coordinated with six water molecules, symmetrically H-bonding
    - essential degeneracy between water-water and water-Cl H-bonding, strong similarity in the water and chloride electronic structure
  - reference https://doi.org/10.1080/00268976.2015.1059959
    - PBE vdW XC AIMD, sixfold Cl-O coordination is dominated, in the first solvation shell surrounding the Cl- ion
    - O-Cl-O angular distribution showing $theta\approx 75 \degree$, indicating **distorted** trigonal prismatic structures

# 2025-05-26
energy diagram drawing

atomic model
- /May26

results
- atomic model
- free energy (formation energy differnece)
  - cuh2o6l5
  - cuh2o6l41
  - cuclh2o5
  - cucl2h2o4
  - cu(I)cl
  - cucl(I)h2o
  - cu(I)cl2
- Win11: Desktop/Cuion/model-2025May26/results_2025May26

doing:
- Cl(H2O)6

not yet done:
- 3W2Cl
  - modeling
- 4W1Cl1
- 4W1Cl2
- 5W5L

# 2025-05-27
doing:
- Cl(H2O)6
  - relaxing
- 3W2Cl
  - relaxing
- 4W1Cl1
  - relaxing
- 4W1Cl2
  - relaxing
- 5W5L
  - relaxing
- methods
- SI
  - graphing

-----
# Results
## singleatom
singlecu2=-401.96197944
singlecu1=-403.07135668
singlecl=-34.88951178
singleh2o=-44.04153750
singlebr=-46.83642638

## Cu2+
### 5L
- 3W2Cl
  - [CuCl2(H2O)3]0
  - cucl2h2o3=-605.21675997
  - cucl2h2o3-singlecu2-singlecl\*2-singleh2o\*3
  - -1.3511444700000368
  - -18.38326632
- 4W1Cl1
  - [CuCl(H2O)4]1+
  - cuclh2o4l1=-614.15869898
  - cuclh2o4l1-singlecu2-singlecl-singleh2o*4
  - -1.1410577600000806
  - -15.52488957
- 4W1Cl2
  - [CuCl(H2O)4]1+
  - cuclh2o4l2=-614.13798055
  - cuclh2o4l2-singlecu2-singlecl-singleh2o*4
  - -1.1203393299999789
  - -15.24300082
- 5W5L
  - [Cu(H2O)5]2+
  - cuh2o5=-622.85887760
  - cuh2o5-singlecu2-singleh2o*5
  - -0.6892106600000432
  - -9.377193477

### 6L
- 4W2Cl1
  - [CuCl2(H2O)4]0
  - cucl2h2o41=-649.32743653
  - cucl2h2o41-singlecu2-singlecl\*2-singleh2o\*4
  - -1.4202835300000345
  - -19.32395162
- 4W2Cl2
  - [CuCl2(H2O)4]0
  - cucl2h2o42=-649.31965224
  - cucl2h2o42-singlecu2-singlecl\*2-singleh2o\*4
  - -1.4124992400000167
  - -19.21804090966823
- 5W1Cl
  - [CuCl(H2O)5]1+
  - cuclh2o5=-658.25247725
  - cuclh2o5-singlecu2-singlecl-singleh2o*5
  - -1.1932985299999928
  - -16.23566181
- 6W4L1
  - [Cu(H2O)6]2+
  - cuh2o6l41=-666.99439952
  - cuh2o6l41-singlecu2-singleh2o*6
  - -0.7831950800000413
  - -10.6559173
- 6W4L2
  - [Cu(H2O)6]2+
  - cuh2o6l42=-667.06330550
  - cuh2o6l42-singlecu2-singleh2o*6
  - -0.8521010599999954
  - -11.59343139
- 6W5L
  - [Cu(H2O)6]2+
  - cuh2o6l5=-667.01612658
  - cuh2o6l5-singlecu2-singleh2o*6
  - -0.8049221400000306
  - -10.95152916

## Cu1+
- 0W1Cl+1
  - [CuCl]0
  - cucl=-438.29948177
  - cucl-singlecu1-singlecl
  - -0.3386133099999924
  - -4.607071112
- 1W1Cl+1
  - [CuClH2O]0
  - cuclh2o=-482.42694170
  - cuclh2o-singlecu1-singlecl-singleh2o
  - -0.42453573999998184
  - -5.776105918
- 0W2Cl+1
  - [CuCl2]1-
  - cucl2=-473.36700849
  - cucl2-singlecu1-singlecl*2
  - -0.5166282499999824
  - -7.029088981
- 0W2Br+1
  - [CuBr2]1-
  - cubr2=-497.80633664
  - cubr2-singlecu1-singlebr*2
  - -1.0621271999999777
  - -14.450984045039698


## Cl-1
- Cl6W-1
  - [Cl(H2O)6]1-
  - clh2o6=-299.28590227
  - clh2o6-singlecl-singleh2o*6
  - -0.14716549000002033
  - -2.002289507


# Reference
- 2+ CuH2O and CuClH2O different configuration
  - reference https://pubs.acs.org/doi/abs/10.1021/jp1000804
- 2+ CuCl2H2O different configuration
  - reference https://pubs.acs.org/doi/10.1021/jp909092p
- DFT calculation MIT Chem
  - https://doi.org/10.1021/acs.jpclett.2c01026
  - B3LYP
  - single point
- 1+ Cu
  - XAFS 2000
    - https://doi.org/10.1016/S0009-2614(00)01110-6
    - Cu1+ linear monochloro and dichloro species
    - no observes of chloride with higher coordination
  - AIMD 2007 Sherman
    - https://doi.org/10.1016/j.gca.2006.09.015
    - predict CuCl3 and CuCl4 at high concentration
  - AIMD 2013 Mei
    - https://doi.org/10.1016/j.gca.2012.10.027
    - low formation constant of CuCl3
  - XAS 2007 Brugger
    - https://doi.org/10.1016/j.gca.2007.08.003
    - only at very high concentration
  - Raman 2013 Applegarth
    - https://doi.org/10.1021/jp406580q
    - CuCl3 only at very high concentration
    - dft predicted linear
    - but dft can predict CuCl3 structure
- Cl-
  - reference https://doi.org/10.1039/C3CP50652E
    - chloride ion prefer coordinated with six water molecules, symmetrically H-bonding
    - essential degeneracy between water-water and water-Cl H-bonding, strong similarity in the water and chloride electronic structure
  - reference https://doi.org/10.1080/00268976.2015.1059959
    - PBE vdW XC AIMD, sixfold Cl-O coordination is dominated, in the first solvation shell surrounding the Cl- ion
    - O-Cl-O angular distribution showing $theta\approx 75 \degree$, indicating **distorted** trigonal prismatic structures
# 2025-06-03
ADF in AMS
- Task - Geometry Optimization
- Frequencies - Yes
- Total charge
- Unrestricted - Yes
- XC functional - Hybrid:B3LYP
- Basis set - QZ4P
- Frozen core - None
- Numerical quality - Normal
- Properties
  - Thermodynamics
    - Pressure - 1.0 atm
    - Temperatures - 298.15 K

can get
- Entropy (cal/mol-K)
- Energy from Engine (eV)
- Internal Energy U (eV)
- Gibbs free energy (eV)
## 6W4L1
- Entropy (cal/mol-K)
  - 119.220
- Energy from Engine (eV)
  - -89.2638
- Internal Energy U (eV)
  - -84.7040 
- Gibbs free energy (eV)
  - -86.2197

## 5W1Cl
- Entropy (cal/mol-K)
  - 126.074
- Energy from Engine (eV)
  - -85.9135
- Internal Energy U (eV)
  - -82.0349
- Gibbs free energy (eV)
  - -83.6392

## 4W2Cl
- Entropy (cal/mol-K)
  - 115.666
- Energy from Engine (eV)
  - -78.9343
- Internal Energy U (eV)
  - -75.7699 
- Gibbs free energy (eV)
  - -77.2396

## 0W1Cl+1
- Entropy (cal/mol-K)
  - 56.645
- Energy from Engine (eV)
  - -5.3202 
- Internal Energy U (eV)
  - -5.2226   
- Gibbs free energy (eV)
  - -5.9292

## 1W1Cl+1
- Entropy (cal/mol-K)
  - 72.495
- Energy from Engine (eV)
  - -23.6026
- Internal Energy U (eV)
  - -22.7601
- Gibbs free energy (eV)
  - -23.6717

## 0W2Cl+1
- Entropy (cal/mol-K)
  - 68.008
- Energy from Engine (eV)
  - -13.2151
- Internal Energy U (eV)
  - -13.0357
- Gibbs free energy (eV)
  - -13.8893

# 2025-07-09
CuBr2 +1

/cucl/Br/Jun26

# 2025-08-01
pva chain with 20 monomer [ATB](https://atb.uq.edu.au/molecule.py?molid=1536128)

use the SMILES code and convert to .pdb [smiles2pdb](https://www.novoprolabs.com/tools/smiles2pdb)

download .pdb file and convert to lammps file .lmp [ligpargen](https://zarbi.chem.yale.edu/ligpargen/)

# 2025-08-05
Cu2+ and Cl- LJ parameters, SPC/E water model

- Cu2+ 
  - [DOI](https://doi.org/10.1021/ct400146w)
    - table 6
  - $\varepsilon=0.00044254$ in kcal/mol
  - $R_{min}/2=1.149$ in $\AA$
    - $\sigma=\frac{R_{min}}{2}\cdot2^{\frac{5}{6}}=2.0472852542865$ in $\AA$
- Cl-
  - [DOI](https://doi.org/10.1021/jp8001614)
    - table 5
  - $\varepsilon=0.012 7850$ in kcal/mol
  - $R_{min}/2=2.711$ in $\AA$
    - $\sigma=\frac{R_{min}}{2}\cdot2^{\frac{5}{6}}=4.830452849756919$ in $\AA$
  
be careful on the LJ expression in the papers, which may be sometimes different from the one in LAMMPS

in LAMMPS:

$$U_{ij}(r_{ij})=4\varepsilon_{ij}[(\frac{\sigma_{ij}}{r_{ij}})^{12}-(\frac{\sigma_{ij}}{r_{ij}})^6]$$

but in the above two papers:

$$U_{ij}(r_{ij})=\varepsilon_{ij}[(\frac{R_{min,ij}}{r_{ij}})^{12}-2(\frac{R_{min,ij}}{r_{ij}})^6]$$

there is a conversion:

$$R_{min}=\sigma\cdot2^{\frac{1}{6}}$$

$$\sigma=\frac{R_{min}}{2}\cdot2^{\frac{5}{6}}$$
- `*2**(5/6)

according to [Texler](http://doi.org/10.1039/A704670G), Cu2+ charge is 2 while Cl- is -1

Lorentz-Berthelot mixing rules

# 2025-08-07
- 4W2
  - [CuBr2H2O4]0
  - cubr2h2o4 = -673.76243465
  - cubr2h2o4-singlecu2-singlebr\*2-singleh2o\*4
  - -1.9614524500000527
  - -26.68693359896572
- 5W1
  - [CuBrH2O5]+1
  - cubrh2o5 = -670.47397170
  - cubrh2o5-singlecu2-singlebr-singleh2o\*5
  - -1.467878380000002
  - -19.971512874766027
