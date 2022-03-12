"""
@author: DukeEgr93
"""

# %% Initialize workspace
import numpy as np
from poly_root import calc_root
import matplotlib.pyplot as plt

# %% Generate guesses and start lists
xi = np.linspace(0, 5, 1000)
rootlist = []
iterlist = []

# %% Run program in a loop and store roots and number of iterations
for init in xi:
    out = calc_root(init, 1e-12, 1000)
    rootlist += [out[0]]
    iterlist += [out[2]]

# %% Make figure with function and map
fig0, ax0 = plt.subplots(2, 1, num=0, clear=True)
fig0.set_size_inches(6, 8, forward=True)
ax0[0].plot(xi, xi ** 3 - 7 * xi ** 2 + 14 * xi - 8, "k-")
ax0[0].grid(True)
ax0[0].set(title="Function", ylabel="$f(x)$", xlabel="$x$")

ax0[1].plot(
    xi,
    (2 * xi ** 3 - 7 * xi ** 2 + 8) / (3 * xi ** 2 - 14 * xi + 14),
    "r-",
    label="map",
)
ax0[1].plot(xi, xi, "k:", label="new=old line")
ax0[1].set_ylim([-10, 10])
ax0[1].set(title="Map to Find Roots", ylabel="$x_{k+1}$", xlabel="$x_k$")
ax0[1].legend(loc=0)

fig0.tight_layout()
fig0.savefig("RootPlot0.png")

# %% Make figure with roots and iteration counts
fig1, ax1 = plt.subplots(2, 1, num=1, clear=True)
fig1.set_size_inches(6, 8, forward=True)

ax1[0].plot(xi, rootlist, "k.")
ax1[0].set(title="Root Estimate", ylabel="Root", xlabel="Initial Guess")

ax1[1].plot(xi, iterlist, "k.")
ax1[1].set(title="Iteration Count", ylabel="Iterations", xlabel="Initial Guess")

fig1.tight_layout()
fig1.savefig("RootPlot1.png")

# %% Visualize roots and interation counts differently
fig2, ax2 = plt.subplots(2, 1, num=2, clear=True)
fig2.set_size_inches(6, 8, forward=True)
rli = ax2[0].imshow(np.array([rootlist]), aspect="auto", extent=(xi[0], xi[-1], 0, 1))
ax2[0].set_yticklabels([])
fig2.colorbar(rli, ax=ax2[0])
ax2[0].set(title="Root Estimate", xlabel="Initial Guess")

tli = ax2[1].imshow(np.array([iterlist]), aspect="auto", extent=(xi[0], xi[-1], 0, 1))
ax2[1].set_yticklabels([])
fig2.colorbar(tli, ax=ax2[1])
ax2[1].set(title="Iteration Count", xlabel="Initial Guess")

fig2.tight_layout()
fig2.savefig("RootPlot2.png")
