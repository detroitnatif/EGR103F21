# %% Import modules
import numpy as np
from fitting_common import *


# %% Load and manipulate data
x, y, xmodel = get_beam_data()
 
# %% Perform calculations
n = 2
p = np.polyfit(x, y, n)
print(p)








# %% Generate estimates and model
yhat = np.polyval(p, x)
ymodel = np.polyval(p, xmodel)

# %% Calculate statistics
calc_stats(y, yhat, 1)

# %% Generate plots
make_plot(x, y, yhat, xmodel, ymodel)