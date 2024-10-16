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
freq=1.0e6
amp=2.0e6
tend=10*(1/freq)

#BUBBLE
R0=np.logspace(-7.5,-4.0,5)
RPmodel='RPAR'
Pambient=1.0e5

#GAS
EoSgas='IG'
Prefgas=Pambient
PolyExp=1.4

#FLUID
Prefliq=Pambient
Rhoref=1000
SSref=1475
Viscosity=np.logspace(-3,-0.35,5)

#INTERFACE
SurfaceTensionCoeff=0.073
LipidCoatingModel='None'
