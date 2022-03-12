#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:15:12 2021

@author: tylerklimas
[graphtemps.py]
[Tyler Klimas]
[9-19-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

from chapra_0304 import daily_temp 
import matplotlib.pyplot as plt
import numpy as np


miami_days = daily_temp('Miami', np.arange(0, 365))
yuma_days = daily_temp('Yuma', np.arange(0, 365))
bismarck_days = daily_temp('Bismarck', np.arange(0, 365))
seattle_days = daily_temp('Seattle', np.arange(0, 365))
boston_days = daily_temp('Boston', np.arange(0, 365))
durham_days = daily_temp('Durham', np.arange(0, 365))
fig = plt.figure(num=1, clear=True)
fig.set_size_inches(6, 6, forward=True)
ax = fig.add_subplot(1,1,1)
x = np.arange(0,365)
ax.plot(x, miami_days, 'm^-', markevery=50, label='Miami')
ax.plot(x, yuma_days, 'yh-', markevery=50, label="Yuma")
ax.plot(x, bismarck_days, 'bs--', markevery=50, label='Bismarck')
ax.plot(x, seattle_days, 'co-', markevery=50, label='Seattle')
ax.plot(x, boston_days, 'g-.', markevery=50, label='Boston')
ax.plot(x, durham_days, 'r^-', markevery=50, label='Durham')
ax.set(title="Months vs Avg Tempature (Tk206",
       xlabel="Days",
       ylabel="Avg Temp")
plt.legend(loc='best')
plt.show
fig.tight_layout()
fig.savefig('graphtemps2.png')
