#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[Fractal.py]
[Tyler Klimas]
[10-17-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np
import matplotlib.pyplot as plt

m = [2]
n = [1]

for i in range(1, 10001):
    q = np.random.uniform(0, 3)
    if q < 1:
        m.append(m[-1]/2)
        n.append(n[-1]/2)
    elif q < 2:
        m.append(m[-1]/2)
        n.append((n[-1]+300)/2)
    else: 
        m.append((m[-1]+300)/2)
        n.append((n[-1]+300)/2)
    ma = np.array(m)
    na = np.array(n)

def normalized(v):
    jm = np.reshape(v, (-1,1))
    return (jm-jm.min())/(jm.max()-jm.min())


fig = plt.figure(num = 1, clear = True)
fig.set_size_inches(6, 6, forward=True)


fig = plt.figure(num = 2, clear = True)
plot1 = fig.add_subplot(1, 1, 1)
plot1.scatter(ma, na, s=1, marker='.')
fig.tight_layout()
fig.savefig('plot1.png')

fig = plt.figure(num = 3, clear = True)
plot2 = fig.add_subplot(1, 1, 1)
plot2.scatter(ma, na, c = na*ma, cmap = 'magma', marker='.', s=1)
fig.tight_layout()
fig.savefig('plot2.png')

fig = plt.figure(num = 4, clear = True)
plot3 = fig.add_subplot(1, 1, 1)
chooseyacolor = np.random.uniform(0, 1, (ma.size, 1))
plot3.scatter(ma, na, c=chooseyacolor, marker='.', s=1)
fig.tight_layout()
fig.savefig('plot3.png')

ma2 = normalized(ma)
na2 = normalized(na)
greenbean = np.block([na2*0, 1-na2, na2*0])

fig = plt.figure(num = 5, clear = True)
plot4 = fig.add_subplot(1, 1, 1)
plot4.scatter(ma, na, c = greenbean, marker='.', s=1)
fig.tight_layout()
fig.savefig('plot4.png')

fig = plt.figure(num=6, clear=True)
plot5 = fig.add_subplot(1,1,1)
redmap = np.block([na2, ma2, ma2*.5])
plot5.scatter(ma, na, c=redmap, marker='o', s=1)
fig.tight_layout()
fig.savefig('plot5.png')










