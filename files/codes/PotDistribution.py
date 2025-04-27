# -*- coding: utf-8 -*-
# Date 2024Dec28
# =============================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os
import plotly.graph_objects as go

fig = plt.figure(figsize=(8,4), dpi=200)
ax = fig.add_subplot(111)
figgo = go.Figure()
plt.style.use("default")
plt.rcParams["lines.linewidth"] = 2
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["xtick.major.width"] = 1
plt.rcParams["ytick.major.width"] = 1
plt.rcParams["xtick.minor.width"] = 1
plt.rcParams["ytick.minor.width"] = 1
xmajorLocator = MultipleLocator(5)
ax.xaxis.set_major_locator(xmajorLocator)
ymajorLocator = MultipleLocator(5)
ax.yaxis.set_major_locator(ymajorLocator)
font = FontProperties(fname="../arial.ttf", size=12)
colormap = ["#d7d5d5", "#383c58", "#68b882"]

ConvRy2eV = 13.605703976
ConvBohr2Ang = 0.529177

# =========================== need change ========================================
input_file = ''                       # avg.dat produced by average.x
nscf_file = ''                        # nscf.out file
# =========================== need change ========================================

work_dir = input_file[:len(input_file)-input_file[::-1].index('/')]
input_file = input_file[len(input_file)-input_file[::-1].index('/'):]
os.chdir(work_dir)

z = []
xy = []
with open(input_file,'r') as f:
    contents = f.readlines()
for line_index, line in enumerate(contents):
    if line_index == 1:
        step=float(line.split()[0])
    try:
        float(line.split()[0])
    except ValueError:
        continue
    except IndexError:
        continue
    linesplit = line.split()
    z.append(float(linesplit[0]))
    xy.append(float(linesplit[1]))
z=np.array(z)*ConvBohr2Ang          # z position
xy=np.array(xy)*ConvRy2eV           # raw, planar average xy plane potential [::-1] for reversed
zavg=[]                             # macroscopic potential, considered crysal periodicity
step = step*ConvBohr2Ang
xend = float(line.split()[0])*ConvBohr2Ang

# Fermi level
with open(nscf_file,'r') as f:
    contents = f.readlines()
for line_index,line in enumerate(contents):
    try:
        line.split().index('Fermi')
    except ValueError:
        continue
    except IndexError:
        continue
    efermi = float(line.split()[-2])
    break
ax.hlines(efermi,0,xend,linestyle='dashed',color=colormap[2],label='Fermi Level')

# =========================== need change ========================================
pt1 = 250        # first point dividing outside/inside slab, 0 = not dividing
pt2 = 1800
pt3 = len(xy)
wid1 = 10        # averaging length outside slab
wid2 = 138       # averaging length inside slab, evaluated by period/step
# =========================== need change ========================================

# =========================== averaging ==========================================
for i in range(pt1):
    group = [-int(wid1/2)+1+j+i for j in range(wid1-1)]
    for ele in group:
        if not(0<ele<pt1-1):
            group.remove(ele)
    zavg.append(1/len(group)*xy[group].sum())
for i in range(pt1,pt2):
    group = [-int(wid2/2)+1+j+i for j in range(wid2-1)]
    for ele in group:
        if not(pt1<ele<pt2-1):
            group.remove(ele)
    zavg.append(1/len(group)*xy[group].sum())
for i in range(pt2,pt3):
    zavg.append(xy[i])  # Not averaging
# =========================== averaging ==========================================

ax.plot(z,xy,label='Planar average',color=colormap[0],linewidth=1)
ax.plot(z,zavg,label='Macroscopic average',color=colormap[1])

# Work function
# =========================== need change ========================================
arrowx=3.5       # location of the arrow
# =========================== need change ========================================

ax.annotate('',xy=(arrowx,efermi-0.4),xytext=(arrowx,xy[int(arrowx/step)]+0.3),arrowprops=dict(arrowstyle="<->",linewidth=1.5))
workfunction=xy[int(arrowx/step)]-efermi
ax.text(arrowx-1.5,xy[int(arrowx/step)]+0.5,r"  $W_F$="+'\n'+f"{workfunction:.2f} eV",fontsize=14,fontproperties=font)

ax.tick_params(which="major", direction="in", labelsize=15, length=7)
ax.tick_params(which="minor", direction="in", length=5)

axxlabel = r"Position (z) [$\rm \AA$]"
ax.set_xlabel(axxlabel, fontsize=15, fontproperties=font)
ax.set_xlim([0, xend])

axylabel = "Electrostatic Potential [eV]"
ax.set_ylabel(axylabel, fontsize=15, fontproperties=font)
ax.set_ylim([ax.get_ylim()[0]-10,ax.get_ylim()[1]+8])
ax.legend(prop=font,loc='upper center')

# fig.savefig('PotDistribution.png',transparent='True',bbox_inches='tight')

figgo.add_trace(go.Scatter(x=z,y=xy))
figgo.add_trace(go.Scatter(x=z,y=zavg))
figgo.add_trace(go.Scatter(x=np.linspace(z[0],z[-1],1000),y=[efermi]*1000))
figgo.show()