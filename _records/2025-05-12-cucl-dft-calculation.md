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
calculate the free energy of 2-valence [Cu(H2O)6]+2, [CuCl2(H2O)4]0 and 1-valence [CuCl2]-1
- unit in Ry

[Cu(H2O)6]+2
=====
- /cucl/May17
cuh2o6=-667.01699261
cuh2o6-singlecu2-singleh2o*6=1.0192963599999985

[CuCl2(H2O)4]0
=====
- /cucl/May20
cucl2h2o4=-649.2832618
cucl2h2o4-singlecu2-singleh2o*4-singlecl*2=-0.12783812999998645

[CuCl2]-1
=====
- /cucl/May23/0W2Cl+1
cucl2=-473.36700849
cucl2-singlecu1-singlecl*2=

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
drawing
- color
  - Cu2+
    - #650065
  - O
    - #7E7E7E
  - H
    - #BFBFBF

# 2025-05-25
- maybe not correct (not pure Cu-Cl complex but with other atoms)
- Cu(I)Cl2 bond distance (Cu-Cl) = 2.104 A
  - angle=175.9deg
- Cu(I)Cl3 bond distance (Cu-Cl) = 2.165+-(12) A
  - angle=120(+-1.5)
reference: https://www.mdpi.com/2304-6740/13/2/36

- Cu(H2O)6 6 coordinations structure
  - bond distance
    - in xy plane = 1.97A
    - z = 2.38A
  - /May25
    - relaxing
reference https://www.sciencedirect.com/science/article/abs/pii/S0009261400011106?fr=RR-2&ref=pdf_download&rr=94538cc13a939b84

- Cu(I) chloride
  - CuCl
    - without water /May25/0W1Cl+1
      - relaxing
    - may have 1 water molecule /May25/1W1Cl+1
      - relaxing
  - CuCl2-
  - CuCl3 2- at 25 C is found but with **very weak bonded Cl-**, at high Cl- concentration
reference: https://doi.org/10.1016/j.gca.2006.09.015

- C