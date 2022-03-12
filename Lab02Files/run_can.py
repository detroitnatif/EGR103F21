# %% import modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# load data
beam_data = pd.read_table('cantilever.dat', header=None)
# copy data into new names
mass = beam_data.iloc[:, 0].copy()
disp = beam_data.iloc[:, 0].copy()

# convert mass to force
force = mass * 9.81
# convert disp to meters
disp = disp * 2.54 / 100


p = np.polyfit(force, disp, 1)
print(p)


force_model = np.linspace(force.min(), force.max(), 100)

disp_model = np.polyval(p, force_model)


# generate plots
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(force, disp, 'ko')
ax.plot(force_model, disp_model, 'b-')



fig.tight_layout()

fig.savefig('RunCanPlot.png')