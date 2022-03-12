#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[oxygen.py]
[Tyler Klimas]
[10-17-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.array([0, 5, 10, 15, 20, 25, 30])
con = np.array([0, 10, 20])
c1 = np.array([14.6, 12.8, 11.3, 10.1, 9.09, 8.26, 7.56])
c2 = np.array([12.9, 11.3, 10.1, 9.03, 8.17, 7.46, 6.85])
c3 = np.array([11.4, 10.3, 8.96, 8.08, 7.35, 6.73, 6.2])

q = np.vstack([c1, c2, c3]).T



m, i = np.meshgrid(con, t)
qx = np.reshape(q, (-1,1))
tx = np.reshape(t, (-1,1))
c11 = np.reshape(c1, (-1, 1))
c21 = np.reshape(c2, (-1, 1))
c31 = np.reshape(c3, (-1, 1))
ii = np.reshape(i, (-1, 1))
mx = np.reshape(m, (-1, 1))




def xfun(g, tem, coefs):
    return coefs[0]+coefs[1]*tem+coefs[2]*g


eq2 = np.block([[mx**0, mx**1, ii**1]])
b = np.linalg.lstsq(eq2, qx, rcond=None)[0]
out1 = xfun(12, 15, b)
per1 = ((abs(out1-9.09)/9.09)*100)

eq3 = np.block([[tx**3,tx**2, tx**1, tx**0]])
c = np.linalg.lstsq(eq3, c11, rcond=None)[0]


def zfun(g, tem, coefs):
    return (coefs[0] + coefs[1]*g +
            coefs[2]*g**2 + coefs[3]*g**3 + coefs[4]*tem)
eq1 = np.block([[ii**0, ii**1, ii**2, ii**3, mx]])
a = np.linalg.lstsq(eq1, qx, rcond=None)[0]

output = zfun(12, 15, a)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
fig.set_size_inches(6,4, forward=True)
xmod=np.linspace(t.min(), t.max(), 100)
pl = c[0]*xmod**3 + c[1]*xmod**2 + c[2] * xmod**1 + c[3]*xmod**(0)
ax.plot(xmod, pl, 'k-')
ax.plot(tx, c11, 'o')
ax.grid(True)
ax.set(xlabel = 'Tempature', 
       ylabel = 'Disolved Oxygen mg/l',
       title = 'Disolved Oxygen vs Tempature with concentration of chloride=0')
fig.tight_layout()
fig.savefig('oxygen.png')

























