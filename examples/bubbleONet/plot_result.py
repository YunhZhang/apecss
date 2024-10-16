import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']=['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=10

cm = 1/2.54

Bubble = np.genfromtxt("results/RP_R1.000e-05_fa2.140e+04_pa1.320e+05.txt", delimiter=" ")

# fig1 = plt.figure(figsize=(30*cm,30*cm))
fig1, ax3 = plt.subplots(figsize=(25*cm, 15*cm)) 
# fig1 = plt.figure()
# numofsubplot = (3,1)
# ax1 = plt.subplot2grid(numofsubplot,(0,0),colspan=1)
# ax2 = plt.subplot2grid(numofsubplot,(1,0),colspan=1)
# ax3 = plt.subplot2grid(numofsubplot,(2,0),colspan=1)
# plt.subplots_adjust(wspace=1.2*cm,hspace=1.2*cm)

# ax1.set(xlabel=r'$t$ [$\mu$s]',ylabel=r'$R(t)$ [$\mu$m]')
# ax1.set_xlim(xmin=0,xmax=60)
# ax1.grid(color='gainsboro', linestyle='-', linewidth=0.5)
# ax1.plot(Bubble[:, 1]*1e6, Bubble[:, 3]*1e6, linestyle='solid', linewidth=1,color='steelblue')

# ax2.set(xlabel=r'$t$ [$\mu$s]',ylabel=r'$\dot{R}(t)$[m/s]')
# ax2.set_xlim(xmin=0,xmax=60)
# ax2.grid(color='gainsboro', linestyle='-', linewidth=0.5)
# ax2.plot(Bubble[:, 1]*1e6, Bubble[:, 4], linestyle='solid', linewidth=1,color='steelblue')

# ax3.set(xlabel=r'$t$ [$\mu$s]',ylabel=r'$p_\mathrm{G}(t)$ [kPa]')
ax3.set_xlabel(r'$t$ [$\mu$s]', fontsize=20)
ax3.set_ylabel(r'$p_\mathrm{G}(t)$ [kPa]', fontsize=20)
ax3.set_xlim(xmin=0,xmax=60)
ax3.grid(color='gainsboro', linestyle='-', linewidth=0.5)
ax3.plot(Bubble[:, 1]*1e6, Bubble[:, -1]/1e3, linestyle='solid', linewidth=2.0,color='steelblue')

# ax1.xaxis.set_label_coords(0.5,-0.24)
# ax2.xaxis.set_label_coords(0.5,-0.24)
# ax3.xaxis.set_label_coords(0.5,-0.24)

# ax1.yaxis.set_label_coords(-0.28, 0.5)
# ax2.yaxis.set_label_coords(-0.25, 0.5)
# ax3.yaxis.set_label_coords(-0.25, 0.5)

folder_path = "plots"
file_name = "ultrasound_valiONet.png"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
full_path = os.path.join(folder_path, file_name)
fig1.savefig(full_path, bbox_inches='tight', pad_inches=0.035)
