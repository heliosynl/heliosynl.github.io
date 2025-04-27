# -*- coding: utf-8 -*-
# Date 2025Jan07
# =============================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os
import plotly.graph_objects as go

fig = plt.figure(figsize=(8,5), dpi=1000)
ax = fig.add_subplot(111)
figgo = go.Figure()
plt.style.use("default")
plt.rcParams["lines.linewidth"] = 2
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["xtick.major.width"] = 1
plt.rcParams["ytick.major.width"] = 1
plt.rcParams["xtick.minor.width"] = 1
plt.rcParams["ytick.minor.width"] = 1
xmajorLocator = MultipleLocator(2)
ax.xaxis.set_major_locator(xmajorLocator)
ymajorLocator = MultipleLocator(2)
ax.yaxis.set_major_locator(ymajorLocator)
font = FontProperties(fname="../arial.ttf", size=12)
colormap = ["#A4A4A4", "#25346B", "#121212", "#7ad1e4" , "#f46c68","#f3ecdd"]

ConvRy2eV = 13.605703976
ConvBohr2Ang = 0.529177

# =========================== need change ========================================
input_file = ''  # .dat.gnu file
nscf_file = ''   # nscf.out file for determining Fermi level
# =========================== need change ========================================
work_dir = input_file[:len(input_file)-input_file[::-1].index('/')]
input_file = input_file[len(input_file)-input_file[::-1].index('/'):]
os.chdir(work_dir)

# =========================== need change ========================================
# Format:
# label="""
# Gamma
# K
# M
# Gamma
# """.split('\n')
label="""
""".split('\n')
# =========================== need change ========================================
label=label[1:-1]
labelpt=[]
for index_ele,ele in enumerate(label):
    if ele == 'Gamma':
        labelpt.append('$\Gamma$')
    else:
        labelpt.append(ele)

# =========================== need change ========================================
# output from plotband.x
# Format:
# kptorder="""
# high-symmetry point:  0.0000 0.0000 0.0000   x coordinate   0.0000
# high-symmetry point:  0.3333 0.5774 0.0000   x coordinate   0.6667
# high-symmetry point:  0.5000 0.2887 0.0000   x coordinate   1.0000
# high-symmetry point:  0.0000 0.0000 0.0000   x coordinate   1.5773
# """.split('\n')
kptorder="""
""".split('\n')
# =========================== need change ========================================
kptorder=kptorder[1:-1]
for index_ele,ele in enumerate(kptorder):
    kptorder[index_ele] = float(kptorder[index_ele].split()[-1])
kptorder=np.array(kptorder,dtype=float).transpose()

kpt = []
bandenergy = [[]]
with open(input_file,'r') as f:
    contents = f.readlines()
flag = 0
for line_index, line in enumerate(contents):
    try:
        float(line.split()[0])
    except IndexError:
        bandenergy.append([])
        flag = 1
        continue
    linesplit = line.split()
    if flag == 0:
        kpt.append(float(linesplit[0]))
    bandenergy[-1].append(float(linesplit[1]))
kpt=np.array(kpt)                     # k points, in relative coordinates, actual coordinates need to take a look on the bands calculation
bandenergy=np.array(bandenergy[:-1])  # band energy, divided by band number
step = kpt[1]-kpt[0]

for index_band, band in enumerate(bandenergy):
    ax.plot(kpt,band,color=colormap[0])
    figgo.add_trace(go.Scatter(x=kpt,y=band,line=dict(color=colormap[0]),showlegend=False))

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
ax.hlines(efermi,kpt[0],kpt[-1],linestyle='dashed',color=colormap[1])
figgo.add_trace(go.Scatter(x=kpt,y=efermi*np.ones(len(kpt)),name='Fermi Level',line=dict(color=colormap[1])))

# =========================== need change ========================================
ylim = [0,10]
# =========================== need change ========================================

# High symmetry points
ax.vlines(kptorder[1:-1],ylim[0],ylim[1],color=colormap[2],linewidth=1)
for pt in kptorder[1:-1]:
    figgo.add_trace(go.Scatter(x=[pt]*2,y=ylim,line=dict(color=colormap[2])))
ax.set_xticks(kptorder)
ax.set_xticklabels(labelpt)

ax.tick_params(which="major", direction="in", labelsize=15, length=7)
ax.tick_params(which="minor", direction="in", length=5)

ax.set_xlim([kpt[0], kpt[-1]])

axylabel = "Energy [eV]"
ax.set_ylabel(axylabel, fontsize=15, fontproperties=font)
ax.set_ylim(ylim)

# fig.savefig('bandstructure.png',transparent='True',bbox_inches='tight')

figgo.update_layout(xaxis=dict(range=[kpt[0], kpt[-1]]),yaxis=dict(range=ylim))
figgo.show()
