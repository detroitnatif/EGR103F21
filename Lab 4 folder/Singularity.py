#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[Singularity.py]
[Tyler Klimas]
[9-19-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt


def singularity(x, a, n):
    return ((x > a) * ((x - a) ** n))
def s(x):
    return -5/6*(singularity(x, 0, 4)) - (singularity(x, 5, 4)) + 5/2*(singularity(x, 8, 3)) + 325/2*(singularity(x, 7, 2))+(79/12*(x**3))-76/3*x

x = np.linspace(0, 10, 100)
y = s(x)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, s(x), 'r-')
ax.set(title="Displacement vs. Distance(ft.) (Tk206)", 
    xlabel="Distance(ft.)",
    ylabel="Displacement")


xVals = np.round(np.linspace(0, 10, int(1e6)), 4)
yVals = np.round(s(xVals), 4)
yMin = min(yVals)
xMin = np.round(xVals[np.where(yVals==yMin)], 4)
xMin_str = str(xMin[0])
yMax = max(yVals)
xMax = xVals[np.where(yVals==yMax)]
xMax_str = str(xMax[0])
 


print("Maximum is " + xMax_str + ', '+ str(yMax))
print('Mininum is ' + xMin_str + ', '+ str(yMin))


ax.grid(True)
fig.tight_layout()
fig.savefig("SingPlots.png")

    

