
import numpy as np
from fitting_common import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

# %% Create data
xm, ym = np.meshgrid(np.arange(-5, 5.1, 5), np.arange(-5, 5.1, 5))
zm = np.random.uniform(size=xm.shape)
xmodelm, ymodelm = np.meshgrid(np.linspace(xm.min(), xm.max(), 21), np.linspace(ym.min(), ym.max(), 21))

# %% Perform calculations
def zfun(xe, ye, coefs):
    return coefs[0] * xe**0 + coefs[1] * xe + coefs[2] * ye + coefs[3] * xe**2 + coefs[4] * xe * ye + coefs[5] * ye**2


# Reshape data for block matrices
xv = np.reshape(xm, (-1, 1))
yv = np.reshape(ym, (-1, 1))
zv = np.reshape(zm, (-1, 1))
phi_mat = np.block([[xv**0, xv, yv, xv**2, xv*yv, yv**2]])
pvec = np.linalg.lstsq(phi_mat, zv, rcond=None)[0]
print(pvec)

# %% Generate estimates and model
zhatv = zfun(xv, yv, pvec) # for stats
zhatm = zfun(xm, ym, pvec) # for graphics
zmodelm = zfun(xmodelm, ymodelm, pvec)

# %% Calculate statistics
calc_stats(zv, zhatv, 1)

# %% Generate plots
# Make model plot
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')

surfhandle = ax.plot_surface(xmodelm, ymodelm, zmodelm, cmap=cm.autumn)
ax.scatter(xm, ym, zm)
ax.set(xlabel='x', ylabel='y', zlabel='z', title='Second Order Model')
fig.colorbar(surfhandle)
fig.tight_layout()

# Make error plot
fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot_surface(xm, ym, zm-zhatm, cmap=cm.autumn)
ax.set(xlabel='x', ylabel='y', zlabel='$z-\hat{z}$', title='Second Order Model Error')
fig.tight_layout()