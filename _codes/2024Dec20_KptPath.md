---
title: "K point Path Generate"
collection: codes
date: 2024-12-20
excerpt: 'Generating K point path by defining the high-symmetry points (in reduced coordinates, irreducible Brillouin zone) and their interval. In QE PWscf format'
codeurl: '/files/codes/KpathGenerate.py'
permalink: /codes/kptpath/
---

```python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os

highsymmypts="""
0.0000000000	0.0000000000	0.0000000000
0.5000000000	0.0000000000	0.0000000000
0.3333333333	0.3333333333	0.0000000000
0.0000000000	0.0000000000	0.0000000000
""".split('\n')
highsymmypts=highsymmypts[1:-1]
for index_ele,ele in enumerate(highsymmypts):
    highsymmypts[index_ele] = highsymmypts[index_ele].split()
highsymmypts=np.array(highsymmypts,dtype=float)

label="""
Gamma
M
K
Gamma
""".split('\n')
label=label[1:-1]
labelpt=[]
for index_ele,ele in enumerate(label):
    labelpt.append(label[index_ele])

kptratio="""
30
20
30
""".split('\n')
kptratio=kptratio[1:-1]
for index_ele,ele in enumerate(kptratio):
    kptratio[index_ele] = kptratio[index_ele]
kptratio=np.array(kptratio,dtype=int).transpose()

kptorder = []
for index_i, i in enumerate(kptratio):
    kptorder.append(kptratio[:index_i].sum())
kptorder.append(kptratio.sum())

kpath = []
for index_pt, pt in enumerate(highsymmypts):
    if index_pt == 0:
        continue
    prev_pt = highsymmypts[index_pt-1]
    for i in range(kptratio[index_pt-1]):
        kpath.append(prev_pt+i*(pt-prev_pt)/kptratio[index_pt-1])
kpath.append(highsymmypts[-1])

print(f"{len(kpath)}")
for index_ele,ele in enumerate(kpath):
    flag = -20
    for index_i, i in enumerate(kptorder):
        if index_ele == i:
            flag = index_i
    if index_ele == 0:
        flag == 0
    elif index_ele == len(kpath)-1:
        flag == len(labelpt)-1
    if flag == -20:
        print(f"{ele[0]:<12.8f}   {ele[1]:<12.8f}   {ele[2]:<12.8f}    {1/len(kpath):.4}")
    else:
        print(f"{ele[0]:<12.8f}   {ele[1]:<12.8f}   {ele[2]:<12.8f}    {1/len(kpath):.4}  !{labelpt[flag]}")
```

## Output
```
81
0.00000000     0.00000000     0.00000000      0.01235  !Gamma
0.01666667     0.00000000     0.00000000      0.01235
0.03333333     0.00000000     0.00000000      0.01235
0.05000000     0.00000000     0.00000000      0.01235
0.06666667     0.00000000     0.00000000      0.01235
0.08333333     0.00000000     0.00000000      0.01235
0.10000000     0.00000000     0.00000000      0.01235
0.11666667     0.00000000     0.00000000      0.01235
0.13333333     0.00000000     0.00000000      0.01235
0.15000000     0.00000000     0.00000000      0.01235
0.16666667     0.00000000     0.00000000      0.01235
0.18333333     0.00000000     0.00000000      0.01235
0.20000000     0.00000000     0.00000000      0.01235
0.21666667     0.00000000     0.00000000      0.01235
0.23333333     0.00000000     0.00000000      0.01235
0.25000000     0.00000000     0.00000000      0.01235
0.26666667     0.00000000     0.00000000      0.01235
0.28333333     0.00000000     0.00000000      0.01235
0.30000000     0.00000000     0.00000000      0.01235
0.31666667     0.00000000     0.00000000      0.01235
0.33333333     0.00000000     0.00000000      0.01235
0.35000000     0.00000000     0.00000000      0.01235
0.36666667     0.00000000     0.00000000      0.01235
0.38333333     0.00000000     0.00000000      0.01235
0.40000000     0.00000000     0.00000000      0.01235
0.41666667     0.00000000     0.00000000      0.01235
0.43333333     0.00000000     0.00000000      0.01235
0.45000000     0.00000000     0.00000000      0.01235
0.46666667     0.00000000     0.00000000      0.01235
0.48333333     0.00000000     0.00000000      0.01235
0.50000000     0.00000000     0.00000000      0.01235  !M
0.49166667     0.01666667     0.00000000      0.01235
0.48333333     0.03333333     0.00000000      0.01235
0.47500000     0.05000000     0.00000000      0.01235
0.46666667     0.06666667     0.00000000      0.01235
0.45833333     0.08333333     0.00000000      0.01235
0.45000000     0.10000000     0.00000000      0.01235
0.44166667     0.11666667     0.00000000      0.01235
0.43333333     0.13333333     0.00000000      0.01235
0.42500000     0.15000000     0.00000000      0.01235
0.41666667     0.16666667     0.00000000      0.01235
0.40833333     0.18333333     0.00000000      0.01235
0.40000000     0.20000000     0.00000000      0.01235
0.39166667     0.21666667     0.00000000      0.01235
0.38333333     0.23333333     0.00000000      0.01235
0.37500000     0.25000000     0.00000000      0.01235
0.36666667     0.26666667     0.00000000      0.01235
0.35833333     0.28333333     0.00000000      0.01235
0.35000000     0.30000000     0.00000000      0.01235
0.34166667     0.31666667     0.00000000      0.01235
0.33333333     0.33333333     0.00000000      0.01235  !K
0.32222222     0.32222222     0.00000000      0.01235
0.31111111     0.31111111     0.00000000      0.01235
0.30000000     0.30000000     0.00000000      0.01235
0.28888889     0.28888889     0.00000000      0.01235
0.27777778     0.27777778     0.00000000      0.01235
0.26666667     0.26666667     0.00000000      0.01235
0.25555556     0.25555556     0.00000000      0.01235
0.24444444     0.24444444     0.00000000      0.01235
0.23333333     0.23333333     0.00000000      0.01235
0.22222222     0.22222222     0.00000000      0.01235
0.21111111     0.21111111     0.00000000      0.01235
0.20000000     0.20000000     0.00000000      0.01235
0.18888889     0.18888889     0.00000000      0.01235
0.17777778     0.17777778     0.00000000      0.01235
0.16666667     0.16666667     0.00000000      0.01235
0.15555556     0.15555556     0.00000000      0.01235
0.14444444     0.14444444     0.00000000      0.01235
0.13333333     0.13333333     0.00000000      0.01235
0.12222222     0.12222222     0.00000000      0.01235
0.11111111     0.11111111     0.00000000      0.01235
0.10000000     0.10000000     0.00000000      0.01235
0.08888889     0.08888889     0.00000000      0.01235
0.07777778     0.07777778     0.00000000      0.01235
0.06666667     0.06666667     0.00000000      0.01235
0.05555556     0.05555556     0.00000000      0.01235
0.04444444     0.04444444     0.00000000      0.01235
0.03333333     0.03333333     0.00000000      0.01235
0.02222222     0.02222222     0.00000000      0.01235
0.01111111     0.01111111     0.00000000      0.01235
0.00000000     0.00000000     0.00000000      0.01235  !Gamma
```