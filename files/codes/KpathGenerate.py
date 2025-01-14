# -*- coding: utf-8 -*-
# Date 2024Dec20
# =============================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os

# =========================== need change ========================================
# Format:
# highsymmypts="""
# 0.0000000000	0.0000000000	0.0000000000
# 0.5000000000	0.0000000000	0.0000000000
# 0.3333333333	0.3333333333	0.0000000000
# 0.0000000000	0.0000000000	0.0000000000
# """.split('\n')
highsymmypts="""
""".split('\n')
# =========================== need change ========================================

highsymmypts=highsymmypts[1:-1]
for index_ele,ele in enumerate(highsymmypts):
    highsymmypts[index_ele] = highsymmypts[index_ele].split()
highsymmypts=np.array(highsymmypts,dtype=float)

# =========================== need change ========================================
# Format:
# label="""
# Gamma
# M
# K
# Gamma
# """.split('\n')
label="""
""".split('\n')
# =========================== need change ========================================

label=label[1:-1]
labelpt=[]
for index_ele,ele in enumerate(label):
    labelpt.append(label[index_ele])

# =========================== need change ========================================
# Format:
# kptratio="""
# 30
# 30
# 20
# """.split('\n')
kptratio="""
""".split('\n')
# =========================== need change ========================================

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