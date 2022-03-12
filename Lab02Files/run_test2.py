#import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#load data
beam_data = pd.read_table('cantilever.dat', header=None)
#copy data into new names
mass = beam_data.iloc[:, 0].copy()
disp = beam_data.iloc[:, 1].copy()
# convert mass to force
force = mass * 9.81
# convert disp to meters
disp = (disp * 2.54) / 100
# generate predictions
p = np.polyfit(force, disp, 1)
print(p)
#generate plots

#create 100 force values
force_model = np.linspace(force.min(), force.max(), 100)
#calculate predictions
disp_model = np.polyval(p, force_model)

#generate plots
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(force, disp, 'ko')
ax.plot(force_model, disp_model, 'b-')

#turn grid on
ax.grid(True)
ax.set_xlabel('Force (Newtons)')
ax.set_ylabel('Displacement (meters)')
ax.set_title('Displacement vs Force for cantilever.dat (TK206)')
fig.tight_layout()

fig.savefig('runcanplot.eps')
fig.savefig('runcanplot.pdf')
fig.savefig('runcanplot.png')

