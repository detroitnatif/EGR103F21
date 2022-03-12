#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:51:09 2021

@author: tylerklimas
"""

def geo_prog(s,e,r):
    try:
        s = float(s)
        e = float(e)
        r = float(r)
    except Exception as uhoh:
        print('All arguments must be single numbers')
        return -1
    try:
         s > 0
         e > 0
         r > 0
    except Exception as uhoh:
        print('All arguments must be positive')
        return -2
    final = []
    n = 1
    num = s
    while num > e:
        num = s * (r**(n-1))
        if num < e:
            break
        final.append(num)
        n=n+1
    return final, sum(final)
    