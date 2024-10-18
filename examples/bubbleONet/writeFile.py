# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:14:03 2024

@author: diego
"""

# This code performs parametric studies of a single isolated bubble 
# interacting with a sinusoidal acoustic wave.

# Date: 4/1/2024

def generateInputFile(fileName, R0, RPmodel, Pambient, EoSgas, Prefgas, PolyExp, Prefliq, Rhoref, SSref, Viscosity, SurfaceTensionCoeff, LipidCoatingModel):
    
    # Open the apecss input file
    with open(fileName, "w") as file:
        
        # Write the header 
        file.write('#########################################################\n\
#                                                       #\n\
#  APECSS Options File                                  #\n\
#                                                       #\n\
#  Input file generated by Diego Vaca                   #\n\
#                                                       #\n\
#########################################################\n\
\n')
        
        # Write the bubble parameters
        file.write('BUBBLE\n\
InitialRadius %.4e\n\
RPModel %s\n\
PressureAmbient %.4e\n\
Dimensionality Sphere\n\
END\n\
\n' % (R0, RPmodel, Pambient))

        # if R0 < 10**(-5.75):
        file.write('ODESOLVER\n\
maxTimeStep 5e-9\n\
minTimeStep 1e-20\n\
END\n\
\n')

        # Write the gas parameters
        file.write('GAS\n\
EoS %s\n\
ReferencePressure %.4e\n\
PolytropicExponent %.4e\n\
END\n\
\n' % (EoSgas, Prefgas, PolyExp))
        
        # Write the liquid parameters
        file.write('LIQUID\n\
LiquidType Newtonean\n\
ReferencePressure %.4e\n\
ReferenceDensity %.4e\n\
ReferenceSoundSpeed %.4e\n\
Viscosity %.4e\n\
END\n\
\n' % (Prefliq, Rhoref, SSref, Viscosity))
        
        # Write the interface parameters
        file.write('INTERFACE\n\
SurfaceTensionCoeff %.4e\n\
LipidCoatingModel %s\n\
END\n\
\n' % (SurfaceTensionCoeff, LipidCoatingModel))
        
        # Write the results parameters
        file.write('RESULTS\n\
Bubble\n\
OutputFreqRP 3\n\
OutputPath ./results\n\
OutputDigits 10\n\
END')
        
    # The file is automatically saved and closed after this block
