---
title: "Python Notes"
date: 2024-12-27
excerpt: 'Coding notes for Python'
type: notes
tags:
  - bash
  - notes
---

Content
=====
{:.no_toc}

* toc
{:toc}

# Python
## import
```python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os
import plotly.graph_objects as go
import scipy as sp
```
## For testing 

```python
a=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
b=np.array([1,2,3]) 
```

## Join elements of list into string with same connector 

`'_'.join(a)`


## Latex coding into string 
`r'$\lambda$' `

## Format string 

- `f'{a}'`
Symbol a will be substitute with value of a in float 
- `f'{abc:f5} `
Character length of 5 
- `f'{abc:>5} `
Justified to the right with character length of 5 
- `f'{abc:<5} `
Justified to the left with character length of 5 

## Write file 

`f = open('filename', mode='w') `

for line in list: 

`f.write(line+'\n') `

Or 

`f.writelines(list) `

## New method: 

```python
with open(input_file, 'r') as f: 
  contents = f.readlines()
for line_index, line in enumerate(contents):
```

```python
with open(input_file, 'w') as f: 
contents = ''.join(contents) 
```

`f.write(contents)`

# Numpy
## Returns the indices that would sort an array. 

- `np.argsort(array_name, axis=0, kind=None, order=None)`
axis=0 sort by row, axis=1 sort by column 
- `np.sort(array_name, axis=0, kind=None, order=None)` 
return sorted array 
- `array[np.argsort(array[2])]`
gives sorted array by array[2]

## Size of array 

`np.size(a, axis=0)`

- axis=0 : number of rows 
- axis=1 : number of columns 

## Delete specific elements of vector 

`np.delete(a, 3) `

3 is index of the element to be deleted 

## Fitting 
```python
p=np.polyfit(x,y,3) cubic fitting 
e=np.linspace(min,max,steps) 
ax.plot(e,np.polyval(p,e)) 
```

### Least square (Ax=>b) 

`np.linalg.lstsq(A,y,rcond=None/'warn') `

Returns a list 
The resulting vector x is [0] 

## Solve a group of linear equations (Ax=b) 

`np.linalg.solve(A,b) `

Returns vector x 

## Higher order Interpolation 

- `f=sp.interpolate.PchipInterpolator(x,y)`
Piecewise Cubic Hermite Interpolating Polynomial 
- `f=sp.interpolate.CubicSpline(x,y)`
- `f=sp.interpolate.make_interp_spline(x,y,k=3) `
- `minimum = sp.optimize.fmin(f,3.1)[0]`

# Matplotlib

```python
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
fig,ax = plt.subplots(1,1,figsize=(6,3), dpi=200, sharex=True, sharey=True,width_ratios=[1])
# axinset = ax.inset_axes([0.37,0.15,0.3,0.5],xlim=(5.9,8.1),ylim=(0.9921,1.0055))
figgo=make_subplots(rows=1,cols=1,insets=[dict(cell=(1,1),w=0.3,l=0.35,h=0.5,b=0.15)])
plt.style.use("default")
plt.rcParams["lines.linewidth"] = 1.5
plt.rcParams["axes.linewidth"] = 0.5
plt.rcParams["xtick.major.width"] = 0.5
plt.rcParams["ytick.major.width"] = 0.5
plt.rcParams["xtick.minor.width"] = 0.5
plt.rcParams["ytick.minor.width"] = 0.5
# xmajorLocator = MultipleLocator(100)
# xminorLocator = MultipleLocator(50)
# ax.xaxis.set_major_locator(xmajorLocator)
# ax.xaxis.set_minor_locator(xminorLocator)
# ymajorLocator = MultipleLocator(100)
# yminorLocator = MultipleLocator(50)
# ax.yaxis.set_major_locator(ymajorLocator)
# ax.yaxis.set_minor_locator(yminorLocator)
font = FontProperties(fname="../Helvetica.ttf", size=10)
```

## Marker
`markermap = ["*", "D", "o", "s", "^"] `

`ax.plot(x, y, marker='*', markersize=20) 
`
Hollow marker: `markerfacecolor='none',markeredgecolor=colormap`

## fill between
ax.fill_between(x,y,0,alpha=0.6) 

## Figure title, label 

- `fig.supxlabel('')`
- `fig.supylabel('')`
- `fig.suptitle(''")` 

## Real Colormap 
```python
colormap = ax.plot(x, y, color=plt.cm.get_cmap('colormapname')(np.linspace(0,1,n))
ax.plot(x, y, color=colormap[num]) 
```

Value of n is depended on how many data point (lines) going to plot 

## Create a twin Axes sharing the xaxis. (Double y axis is created) 
`axes.twinx()` 

## Legend change the sequence/ customize labels 
```python
c = c1 + c2 
labs = [cc.get_label() for cc in c] 
ax.legend(c, labs, loc='upper left', fontsize=14, ncol=3)
```

Or

```python
handles, labels = plt.gca().get_legend_handles_labels() 
plt.legend([handles[i] for i in order], [labels[i] for i in order])  
```

## Vertical line 
`ax.vlines() `

## Y axis on right side 
```python
ax.yaxis.tick_right() 
ax.yaxis.set_label_position('right') 
```

## Texts under x ax (ticks) 
`ax.set_xticklabels() `

## Location of the short lines of x ax (ticks) 
`ax.set_xticks([])`

## Color of frame
- `ax.spines['bottom'].set_color('#dddddd')` 
- `ax.spines['top'].set_color('#dddddd')  `
- `ax.spines['right'].set_color('red') `
- `ax.spines['left'].set_color('red') `
- `ax.spines['left'].set_color('none') `

## Color of ticks 
```python
ax.xaxis.label.set_color('red') 
ax.tick_params(axis='x', colors='red') 
```

## Font setting 
```python
font = FontProperties(fname="YaHei.ttf", size=12) 
ax.plot(x, y, label="Chinese") 
ax.legend(prop=font) 
for index_ele,ele in enumerate(ax.get_yticklabels()): 
  ele.set_fontproperties(font) 
ax.set_title("Chinese", fontsize=18, fontproperties=font)
```

First line of the script above is inserted automatically when initialization py file 

The "size" parameter only influence to the font size of legend 

## Subplots tight 
```python
fig.tight_layout()
fig.subplots_adjust(wspace=0, hspace=0.4) 
```

## Inset plot
```python
axinset = ax.inset_axes([0.35,0.15,0.3,0.5],xlim=(-8.7,-7.8),ylim=(0.94,0.99)) 
ax.indicate_inset_zoom(axinset, edgecolor="black") 
```

## Rectangle 
```python
import matplotlib.patches as patches 
rec=Patches.Rectangle(xy, width, height, angle=0.0,linewidth=1, edgecolor='r', facecolor='none') 
ax.add_patch(rec)
```

## Transparent background 
```python
py_file = __file__
work_dir = py_file[:len(py_file)-py_file[::-1].index('/')]
py_file = py_file[len(py_file)-py_file[::-1].index('/'):]
os.chdir(work_dir)

fig.tight_layout()
plt.savefig('hBNsapphire113KPL.png',transparent=True,bbox_inches='tight')
```

## Remove scientific notation 
`ax.ticklabel_format(style='plain') `

## Scientific notation fontsize 
`ax.yaxis.offsetText.set_fontsize(24)`

## Chinese characters displaying
```python
From matplotlib.font_manager import FontProperties
font = FontProperties(fname="XXX.ttf", size=12) # .ttf is located under same folder with .py
# size=12 only influence ax.legend
ax.plot(x, y, label="Chinese")
ax.legend(prop=font)
ax.set_title("Chinese", fontsize=18, fontproperties=font)
```

## Legend cols, spacing
```python
ax.legend(prop=font,frameon=False,ncol=2,labelspacing=0.2,columnspacing=0.5)
```

# OS 
## input file
```python
input_file = ''
work_dir = input_file[:len(input_file)-input_file[::-1].index('/')]
input_file = input_file[len(input_file)-input_file[::-1].index('/'):]
os.chdir(work_dir)
```

## Change directory 
`os.chdir('path') `
- For Windows, path should be like `'C:\\User\\Desktop\\Temp'`
- For Linux, path should be like `'/home/yongnali08/Desktop/Temp' `

## Get current work directory 
`os.getcwd() `

## List directory 
`os.listdir() `

## Split file name into name part and extension part 
`os.path.splitext(filename)`

Example: `filename.py `

Return of `os.path.splitext('filename.py')` is 'filename' and '.py' 

## Rename file 
`os.rename(original name, new name)`

# NetCDF4 
## Extract Data from .nc 
from netCDF4 import Dataset
```python
nc = Dataset("nc_file_name.nc") 
nc.variables['variable_name'] # output of this terms is an array
```

# Plotly 
## Plot
```python
import plotly.graph_objects as go 
figgo = go.Figure()
figgo.add_trace(go.Scatter(x=x,y=y,name=name,line=dict(color='#000000',width=4),opacity=0.5,mode='markers'))
figgo.add_trace(go.Scatter(x=x2,y=y2,name=name2,line=dict(color='#AAAAAA',width=6),mode='lines'))) 
figgo.add_trace(go.Scatter(x=x,y=y,line_color="#454545")) 
fig.show() 
```

## Subplot
```python
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
figgo = go.Figure() 
figgo=make_subplots(rows=1,cols=1,shared_xaxes=True,vertical_spacing=0.02,insets=[dict(cell=(1,1),w=0.3,l=0.35,h=0.5,b=0.15)]) 
```

## Interactive plot in one line (for interactive window) 
```python
import plotly.graph_objects as go 
go.Figure().add_trace(go.Scatter(x=x,y=y,name=name,line=dict(color='#000000',width=4))).add_trace(go.Scatter(x=x2,y=y2,name=name2,line=dict(color='#AAAAAA',width=6))).show()
```

## Check data, remove line
figgo.data

## Fill between
```python
go.Scatter(x=x,y=y1,fill='tonexty') 
go.Scatter(x=x,y=y2) 
```
Fill area between y2 and y1 (y2>y1) 

```python
go.Scatter(x=x,y=y,fill='tozeroy') 
```
Fill area between y and x axis (y=0) 

## Layout
```python
figgo.update_layout(title=title, xaxis_title=xaxis, yaxis_title=yaxis, legend_title=legend)
figgo.update_layout(legend=dict(y=0.99,x=0.01),xaxis=dict(range=[-10.1,-9.9]),yaxis=dict(range=[0.43,0.52]))
figgo.update_xaxes(type='log') 
figgo.add_trace(go.Scatter(x,y,showlegend=False)) 
```

### subplot layout update
```python
figgo.update_layout(xaxis2=dict(range=[-10.1,-9.9]),yaxis2=dict(range=[0.43,0.52]))
```
xaxis2 yaxis2 for subplot