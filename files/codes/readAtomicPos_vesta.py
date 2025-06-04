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
	cell = []
	elelist = []
	atompos = []
	cellnum = 0
	markcellnum = 0
	strucnum = 0
	atomnum = 0
	for line_index, line in enumerate(f):
	    if cellnum != 0 and strucnum == 0 and markcellnum == 0:
		try:
		    float(line.split()[0])
		except ValueError:
		    continue
		except IndexError:
		    continue
		p=line.split()
		cell.append([float(p[0]),0,0])
		cell.append([float(p[1])*np.sin(np.pi/180*(90-float(p[5]))),float(p[1])*np.cos(np.pi/180*(90-float(p[5]))),0])
		cell.append([0,0,float(p[2])])
		markcellnum = 1
	    elif cellnum != 0 and strucnum != 0:
		try:
		    float(line.split()[0])
		except ValueError:
		    break
		except IndexError:
		    break
		if float(line.split()[0]) != 0:
		    p=line.split()
		    atomnum = int(p[0])
		    try:
		        elelist.index(p[1])
		    except ValueError:
		        elelist.append(p[1])
		        atompos.append([])
		    atompos[elelist.index(p[1])].append([float(p[5]),float(p[4]),float(p[6])])
	    if cellnum == 0:
		try:
		    line.split()[0].index('CELL')
		except ValueError:
		    continue
		except IndexError:
		    continue
		cellnum=line_index
	    else:
		try:
		    line.split().index('STRUC')
		except ValueError:
		    continue
		except IndexError:
		    continue
		strucnum=line_index

cell = np.array(cell)
for index_ele, ele in enumerate(atompos):
    pos=np.array(ele)
    atompos[index_ele] = np.dot(pos,cell)
    atompos[index_ele] = atompos[index_ele][np.argsort(atompos[index_ele][:,2])]
for i in range(len(elelist)):
    for j in range(len(atompos[i])):
        pos=atompos[i][j]
        print(f"{elelist[i]:<6}  {pos[0]:12.8f}      {pos[1]:12.8f}      {pos[2]:12.8f}")
print(f"atom number: {atomnum:.0f}")
