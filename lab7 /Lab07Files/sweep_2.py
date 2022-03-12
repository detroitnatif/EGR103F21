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


v = np.linspace(0, 100, 201)

def sweep_2():
    current = []
    num = []
    for i in v:
        m = np.array([[1, 1, 1, 0, 0, 0],
                       [0, -1, 0, 1, -1, 0],
                       [0, 0, -1, 0, 0, 1],
                       [0,0,0,0,1,-1],
                       [0, i, -10, 0, -15, -5],
                       [5, -i, 0, -20, 0, 0]])
        b = np.array([[0],[0],[0],[0],[0],[200]])
        ans = np.linalg.solve(m, b)
        num.append(np.log10(np.linalg.cond(m, p=None)))
        current.append(ans[1])
    return current, num
q, w = sweep_2()

figa = plt.figure(num=1, clear=True)
ax = figa.add_subplot(1,1,1)
ax.plot(v, q, color = 'orange')
ax.set_xlabel('Ohms $\Omega$')
ax.set_ylabel('Current (A)')
ax.grid(True)
figa.savefig('sweep2figa.png')

figb = plt.figure(num=2, clear=True)
ax = figb.add_subplot(1,1,1)
ax.plot(v, w, color = 'k')
ax.set_xlabel('Ohms $\Omega$')
ax.grid(True)
figb.savefig('sweep2figb.png')
