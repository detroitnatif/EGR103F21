#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:53:52 2021

@author: tylerklimas
[connect_code7.py]
[Tyler Klimas]
[10-21-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np


#7
e = np.matrix([[0, -7, 5], 
               [0, 4, 7],
               [-4, 3, -7]])
k = np.matrix([[50],
               [-30],
               [40]])
print(np.linalg.solve(e, k))

m = np.matrix([[-9/10, -2/10, 1], [-9/9, 1/9, 3/9], [-15/15, 1/15, -6/15]])
print(np.linalg.norm(m, 'fro'))
print(np.linalg.norm(m, 1))
print(np.linalg.norm(m, np.inf))




#11.007

n = np.matrix([[-11, 1, -2],[2, -6, -1], [-3, -1, 7]])
p = np.matrix([[15, -3, -1],[-3, 18, -6], [-4, -1, 12]])
print(np.linalg.norm(n, 'fro'))
print(np.linalg.norm(n, np.inf))
print(np.linalg.norm(p, 'fro'))
print(np.linalg.norm(p, np.inf))

d = np.matrix([[750.5], [300], [102], [20]])
z = np.matrix([[13.422, 0, 0, 0],
               [-13.422, 12.252, 0, 0],
               [0, -12.252, 12.377, 0],
               [0,0,-12.377, 11.797]])
a = np.linalg.cond(z, 'fro')
print(np.linalg.solve(z, d))
print(np.linalg.cond(z, 'fro'))
print(np.log10(a))
