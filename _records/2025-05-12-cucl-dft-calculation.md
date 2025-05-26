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
  - O
    - #7E7E7E
  - H
    - #BFBFBF
  - Cl
    - #1EFFEF

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
        - relaxing
          - cuh2o6l42=
            - cuh2o6l41-singlecu2-singleh2o*6
              - 0
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
  - reference https://pubs.acs.org/doi/abs/10.1021/jp1000804


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
  - need modeling
- 4W1Cl1
- 4W1Cl2
- 5W5L