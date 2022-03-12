#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:39:37 2021

@author: tylerklimas
"""
import numpy as np

A = np.array([[1, -2], [-3, 4]])
print(np.linalg.norm(A))
print(np.linalg.norm(A, 1))
print(np.linalg.norm(A, np.inf))
print(np.linalg.norm(A, 'fro'))
print(np.linalg.norm(A, 2))

c = np.array([[1, 2], [2, 1]])
d = np.array([[1, 2], [2, 1]])

print(np.linalg.inv(c))