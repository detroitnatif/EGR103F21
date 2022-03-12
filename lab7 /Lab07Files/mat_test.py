#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:58:19 2021

@author: tylerklimas
"""

def mat_mult(a, b):
    result = []
    col = len(a[0])
    row = len(b)
    if col != row:
        print('Invalid Sizes')
        return None
    else:
        
        for i in range(0, len(a)):
            ans = []
            for j in range(len(b[0])):
                x = 0
                for k in range(len(b)):
                    x += a[i][k]* b[k][j]
                ans.append(x)
            result.append(x)
    return result
            