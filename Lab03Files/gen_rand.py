# -*- coding: utf-8 -*-
"""
[gen_rand.py]
[Tyler Klimas]
[9-19-21]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

NetID = input("NetID: ")
seed = 0
for code in map(ord, NetID):
    seed = seed + code

np.random.seed(seed)

# %% Number of numbers
nums = int(input('numbers: ')) # Remove 1000 and put your code here

u_d = np.random.uniform(0,1, nums)
n_d = np.random.normal(0,1, nums)
normal_min = '{:.3e}'.format((np.min(n_d)))
normal_max = '{:.3e}'.format((np.max(n_d)))
uniform_min = '{:.3e}'.format((np.min(u_d)))
uniform_max = '{:.3e}'.format((np.max(u_d)))
normal_avg = '{:.3e}'.format(np.mean(n_d))
uniform_avg = '{:.3e}'.format(np.mean(u_d))

num_bins = m.ceil(10 * m.log10(nums))
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.hist(u_d, num_bins)
ax.set(title="Uniform")
fig.tight_layout()
fig.savefig("UniformPlot.png")

fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.hist(n_d, num_bins)
ax.set(title="Normal")
fig.tight_layout()
fig.savefig("NormalPlot.png")
print("Information for " + str(nums) + " random numbers for " + str(NetID) + ':')
print('Uniform: min: ' + str(uniform_min) + ' avg: ' + str(uniform_avg) + ' max: ' + str(uniform_max))
print('Normal: min: ' + str(normal_min) + ' avg: ' + str(normal_avg) + ' max: ' + str(normal_max))
















