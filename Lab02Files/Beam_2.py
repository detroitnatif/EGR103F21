#%[9/9/21]
#Written by: Michael R. Gustafson II

#I understand and have adhered to all the tenets of the Duke Community Standard
#in creating this code.
#Signed: [Tk206]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#load data
beam_2 = pd.read_csv('Beam2.dat', header=0) #pd.read_csv
#copy data into new names
mass = beam_2.iloc[:, 0].copy()
disp = beam_2.iloc[:, 1].copy()
# convert mass to force
force = mass * 9.81
# convert disp to meters
disp = (disp * 2.54) / 100
# generate predictions
p_2 = np.polyfit(force, disp, 1)
print(p_2)
#generate plots

#create 100 force values
force_model = np.linspace(force.min(), force.max(), 100)
#calculate predictions
disp_model = np.polyval(p_2, force_model)
print(disp_model)

#generate plots
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(force, disp, 'ko')
ax.plot(force_model, disp_model, 'b-')

#turn grid on
ax.grid(True)
ax.set_xlabel('Force (Newtons)')
ax.set_ylabel('Displacement (meters)')
ax.set_title('Displacement vs Force for Beam_2.dat (TK206)')
fig.tight_layout()

fig.savefig('Beam2plot.png')
