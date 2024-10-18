# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:14:19 2024

@author: diego
"""

# This code performs parametric studies of a single isolated bubble 
# interacting with a sinusoidal acoustic wave.

# Date: 4/1/2024
import numpy as np

# User input variables
#GLOBAL
freq= np.linspace(20,2000,10) *1000
amp= np.linspace(1,10,10) *1e5
tend= 55e-6

#BUBBLE
R0= np.linspace(1, 100, 11, dtype=int)* 1e-6
RPmodel= 'RP'
Pambient=1.0e5

#GAS
EoSgas='IG'
Prefgas=Pambient
PolyExp=1.4

#FLUID
Prefliq=Pambient
Rhoref=1000
SSref=1475
Viscosity = 0.006

#INTERFACE
SurfaceTensionCoeff=0.072
LipidCoatingModel='None'

#Result
OutputFreqRP=3
OutputPath= './results'
OutputDigits=10