# -*- coding: utf-8 -*-
# Date 2024Dec29
# =============================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import os

# =========================== need change ========================================
input_file = '' # can be scf or nscf, if nscf remember to change line 39&40
work_dir = input_file[:len(input_file)-input_file[::-1].index('/')]
input_file = input_file[len(input_file)-input_file[::-1].index('/'):]
os.chdir(work_dir)
# =========================== need change ========================================

with open(input_file, 'r') as f: 
  contents = f.readlines()
flag = 0
kptnum = 0
kptorder = 0
bands = []
kptlist = []
efermi = 0
for line_index, line in enumerate(contents):
    if flag == 0:                                         # First step:
        try:
            line.index('number of k points=')             # Check number of k points
        except ValueError:
            continue
        except IndexError:
            continue
        flag = 1
        kptnum = int(line.split()[4])
    elif flag == 1:                                              # Second step:
        try:
            line.index('End of self-consistent calculation')     # check where is the end of scf calculation
            # line.index('End of band structure calculation')     # check where is the end of nscf calculation
        except ValueError:
            continue
        except IndexError:
            continue
        flag = 2
    elif flag == 2:                                                       # Third step:
        try:
            line.split().index('k')                                       # get band energy for each k point
        except ValueError:
            continue
        except IndexError:
            continue
        kptlist.append(line[line.index('=')+1:line.index('(')])
        bands.append([])
        for line_index2, line2 in enumerate(contents[line_index+2:]):     # record band energy to bands
            try:
                float(line2.split()[0])
            except ValueError:                                            # prevent if minus sign stick together
                newline2 = []
                for ele in line2:
                    if ele == '-':
                        newline2.append(' -')
                    else:
                        newline2.append(ele)
                newline2 = ''.join(newline2)
                for ele in newline2.split():
                    bands[kptorder].append(float(ele))
                continue
            except IndexError:
                kptorder+=1                                                # finish band energy collection of the present k point
                break
            for ele in line2.split():
                bands[kptorder].append(float(ele))
        if kptorder == kptnum:                                             # finish band energy collection of all k points
            flag = 3
    else:                                           # Fermi energy
        try:
            line.index('the Fermi energy is')
        except ValueError:
            continue
        except IndexError:
            continue
        efermi = float(line.split()[-2])

VBM = efermi - 10
CBM = efermi + 10
bandgapkpt = [0,0]           # [VBM, CBM]
for kpt_index, kpt in enumerate(bands) :
    for eband_index, eband in enumerate(kpt):
        if eband > efermi:
            if eband < CBM:
                CBM = eband
                bandgapkpt[1] = kpt_index
        elif eband < efermi:
            if eband > VBM:
                VBM = eband
                bandgapkpt[0] = kpt_index

bandgap = CBM-VBM

print(f'Bandgap: {bandgap:.4f} eV')
print(f'at k point: VBM:{bandgapkpt[0]:d} ({kptlist[bandgapkpt[0]]}) CBM:{bandgapkpt[1]:d} ({kptlist[bandgapkpt[1]]})')