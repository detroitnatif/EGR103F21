#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 22:17:51 2021

@author: tylerklimas

"""
import numpy as np

def concentrations(c1, c3):
    m = np.array([[6,0,-1,0,0],
                   [-3,3,0,0,0],
                   [0,-1,9,0,0],
                   [0,1,8,-11,2],
                   [3,1,0,0,-4]])
    b = np.array([[5*c1],
                  [0],
                  [8*c3],
                  [0],
                  [0]])
    sol = np.linalg.solve(m,b)
    return sol
    