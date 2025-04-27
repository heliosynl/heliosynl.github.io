# -*- coding: utf-8 -*-
# Date 2024Dec22
# =============================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os

# =========================== need change ========================================
input_file = ''
work_dir = input_file[:len(input_file)-input_file[::-1].index('/')]
input_file = input_file[len(input_file)-input_file[::-1].index('/'):]
os.chdir(work_dir)
# =========================== need change ========================================

fdata=open(input_file,'r')

with open(input_file,'r') as f:
    elelist = []
    atompos = []
    marknum = 0
    atomnum = 0
    for line_index, line in enumerate(f):
        if marknum != 0:
            try:
                float(line.split()[1])
            except ValueError:
                break
            except IndexError:
                break
            p=line.split()
            try:
                elelist.index(p[0])
            except ValueError:
                elelist.append(p[0])
                atompos.append([])
            atompos[elelist.index(p[0])].append([float(p[1]),float(p[2]),float(p[3])])
            atomnum+=1
        try:
            line.split().index('ATOMIC_POSITIONS')
        except ValueError:
            continue
        except IndexError:
            continue
        marknum=line_index


for index_ele, ele in enumerate(atompos):
    atompos[index_ele] = np.array(atompos[index_ele])
    atompos[index_ele] = atompos[index_ele][np.argsort(atompos[index_ele][:,2])]
for i in range(len(elelist)):
    for j in range(len(atompos[i])):
        pos=atompos[i][j]
        print(f"{elelist[i]:<6}  {pos[0]:12.8f}      {pos[1]:12.8f}      {pos[2]:12.8f}")
print(f"atom number: {atomnum:.0f}")
