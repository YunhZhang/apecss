# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:12:32 2024

@author: diego
"""

# This code performs parametric studies of a single isolated bubble 
# interacting with a sinusoidal acoustic wave.

# Parametric study: VISCOSITY vs INITIAL BUBBLE RADIUS

# Date: 4/1/2024

# Import user input values
import os
import time
import numpy as np

# Import user values
from userInputs import R0, RPmodel, Pambient, EoSgas, Prefgas, PolyExp, Prefliq, Rhoref, SSref, Viscosity, SurfaceTensionCoeff, LipidCoatingModel, freq, amp, tend

# Import file generator
from writeFile import generateInputFile

# Generate files in different directories
mainDirectory=os.getcwd()
nSim=0
for j in range(len(Viscosity)):
    for i in range(len(R0)):
        #Directory
        Name="viscosity_"+str(j)+"-radius_"+str(i)
        folderName="results/"+Name
        isdir = os.path.isdir(folderName)
        if (isdir==False): os.mkdir(folderName)  
        
        #File
        fileName=folderName+"/"+Name+".apecss"
        generateInputFile(fileName, R0[i], RPmodel, Pambient, EoSgas, Prefgas, PolyExp, Prefliq, Rhoref, SSref, Viscosity[j], SurfaceTensionCoeff, LipidCoatingModel)
            
        #Execute simulation
        os.chdir(folderName)
        lineCommand='./../../../../build/ultrasound_apecss -options '+Name+ '.apecss -freq '+str(freq)+' -amp '+str(amp)+' -tend '+str(tend)
        #print(lineCommand)
        os.system(lineCommand)
        os.chdir(mainDirectory)
        nSim=nSim+1
        
print(' ')
print('DONE: simulations ran successfully! Total number of simulations: '+str(nSim))

# Calculate energy intensities

# fileavg=open('avgEnergyResults.txt',"w")
# fileavg.write('initialRadius viscosity absortionCoeff qvisc_avg qus_avg\n')
#
# for j in range(len(Viscosity)):
#     for i in range(len(R0)):
#         #Directory
#         Name="viscosity_"+str(j)+"-radius_"+str(i)
#         print(Name)
#         folderName="results/"+Name
#         #File
#         for file in os.listdir(folderName):
#             if file.endswith(".txt"):
#                 fileName=os.path.join(folderName, file)
#
#         #Read results with numpy
#         bubble = np.genfromtxt(fileName, delimiter=" ")
#         sizeVector=len(bubble[:,0])
#         dfltVector = np.zeros(sizeVector)*np.nan
#         mu=Viscosity[j]
#         R=bubble[:,3]
#         dR=bubble[:,4]
#         ddR=np.zeros(len(dfltVector))
#         for k in range(len(ddR)-1):
#             ddR[k+1]=(dR[k+1]-dR[k])/bubble[k+1,2]
#
#         #Calculate q_visc and q_us
#         qvisc = np.zeros(sizeVector)
#         qus = np.zeros(sizeVector)
#
#         absortionCoeff = (11*mu/3)*(1/(Rhoref*SSref**3))*(2*np.pi*freq)**2 # Np/m, assumes mu_b=3*mu
#         #absortionCoeff=18
#
#         for k in range(len(dfltVector)):
#             qvisc[k] = (4*np.pi*R[k]**2)*(4*mu*((dR[k]**2)/R[k])) # from NSF proposal
#             # next equation from R. Glynn Holt & Ronald A. Roy (10.1016/s0301-5629(01)00438-0)
#             P0 = (Rhoref*R[k]/R0[i])*(2*dR[k]**2+R[k]*ddR[k])
#             I0 = P0**2/(2*Rhoref*SSref)
#             qus[k] = (4/3)*(np.pi*R0[i]**3)*2*absortionCoeff*I0
#             # from Glynn Holt: The Good, the Bad, and the Ugly
#             #qus[k] = (Rhoref*absortionCoeff/SSref)*(2*dR[k]**2+R[k]*ddR[k])
#             # from Yukio Kaneko, Heating mechanism of microbubbles and bubble properties
#             #qus[k] = (Rhoref/SSref)*(4*np.pi*R[k]**2)*(2*dR[k]**2+R[k]*ddR[k])**2
#
#         #Energy averages
#         qvisc_avg = 0.0
#         qus_avg = 0.0
#         for k in range(len(dfltVector)):
#             qvisc_avg = qvisc_avg+(bubble[k,2]/tend)*qvisc[k]
#             qus_avg = qus_avg+(bubble[k,2]/tend)*qus[k]
#
#         #Write energy file
#         file1Name=folderName+'/energy_'+"viscosity_"+str(j)+"-radius_"+str(i)+'.csv'
#         file1 = open(file1Name, "w")
#         file1.write('time radius ddradius viscosity qvisc qus\n')
#         for k in range(len(bubble[:,0])):
#             file1.write('%.10e %.10e %.10e %.10e %.10e %.10e\n' % (bubble[k,1], R[k], ddR[k], Viscosity[j], qvisc[k], qus[k]))
#         file1.close()
#
#         #Write averages
#         fileavg.write('%.10e %.10e %.10e %.10e %10e\n' % (R0[i], Viscosity[j], absortionCoeff, qvisc_avg, qus_avg))
#
# fileavg.close()
# print('DONE: qvis and qus were calculated and averaged')
