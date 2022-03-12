#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:53:52 2021

@author: tylerklimas
[sweep_1.py]
[Tyler Klimas]
[10-21-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt


v = np.linspace(0, 400, 101)

def sweep_1():
    current = []
    for i in v:
        m = np.array([[1, 1, 1, 0, 0, 0],
                       [0, -1, 0, 1, -1, 0],
                       [0, 0, -1, 0, 0, 1],
                       [0,0,0,0,1,-1],
                       [0, 10, -10, 0, -15, -5],
                       [5, -10, 0, -20, 0, 0]])
        b = np.array([[0],[0],[0],[0],[0],[i]])
        ans = np.linalg.solve(m, b)
        current.append(ans[1])
    return current
output = sweep_1()
print(output)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.grid(True)
ax.plot(v, output, color = 'purple')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (Amps)')
fig.savefig('sweep1.png')