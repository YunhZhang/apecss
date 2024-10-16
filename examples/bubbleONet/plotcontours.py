# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:34:09 2024

@author: diego
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#matplotlib.use('TkAgg')
#LATEX FONT
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = [r'\usepackage{lmodern}']

#TIMES NEW ROMAN FONT
#plt.rcParams["font.family"] = "Times New Roman"

# User inputs
from userInputs import R0, RPmodel, Pambient, EoSgas, Prefgas, PolyExp, Prefliq, Rhoref, SSref, Viscosity, SurfaceTensionCoeff, LipidCoatingModel, freq, amp, tend

#Import avg qvis and qus
fname="avgEnergyResults.txt"
data_org=pd.read_csv(fname, sep = ' ')
data=data_org

qvisc=np.ones((len(Viscosity),len(R0)))*np.nan
qus=np.ones((len(Viscosity),len(R0)))*np.nan

kloc=0
for i in range(len(Viscosity)):
    for j in range(len(R0)):
        dumVal=data[data.index==kloc]
        qvisc[i,j]=dumVal.qvisc_avg
        qus[i,j]=dumVal.qus_avg
        kloc=kloc+1

#Plot settings
xlab1=r"$ log(R_{0}) \: (m)$"
ylab1=r"$ log(\mu) \: (Pa.s)$"

fs=16
pcolor='black'
sizeHorizontal=9
sizeVertical=8

#Plot qvisc
name1='qvisc_contours'
plt.rc('font', size=16)
fig,ax= plt.subplots(figsize=(sizeHorizontal, sizeVertical))
cs=ax.contourf(np.log10(R0), np.log10(Viscosity), qvisc, np.linspace(min(data.qvisc_avg), max(data.qvisc_avg), num=60), cmap="jet")
cbar = fig.colorbar(cs)
ax.set_ylabel(ylab1, fontsize=fs)
ax.set_xlabel(xlab1, fontsize=fs)
     
plt.tight_layout()  # otherwise the right y-label is slightly clipped
name=name1+'.png'
plt.savefig(name, transparent=True)
name=name1+'.svg'
plt.savefig(name, transparent=True)

#Plot qus
name1='qus_contours'
plt.rc('font', size=16)
fig,ax= plt.subplots(figsize=(sizeHorizontal, sizeVertical))
cs=ax.contourf(np.log10(R0), np.log10(Viscosity), qus, np.linspace(min(data.qus_avg), max(data.qus_avg), num=60), cmap="jet")
cbar = fig.colorbar(cs)
ax.set_ylabel(ylab1, fontsize=fs)
ax.set_xlabel(xlab1, fontsize=fs)
     
plt.tight_layout()  # otherwise the right y-label is slightly clipped
name=name1+'.png'
plt.savefig(name, transparent=True)
name=name1+'.svg'
plt.savefig(name, transparent=True)

plt.show()

print('DONE: contour plot saved')
