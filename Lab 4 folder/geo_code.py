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
        return -1, -1
    if s < 0 or e < 0 or r < 0:
        print('ALL arguments must be positive')
        return -2, -2
    final = []
    n = 1
    num = s
    if r > 1:
        if s > e:
            print('Invalid Sequence')
            return -3, -3
    if r < 1:
        if e > s:
            print('Invalid Sequence')
            return -3, -3
    if r < 1:
        while num > e:
            num = s * (r**(n-1))
            if num < e:
                break
            final.append(num)
            n=n+1
    if r > 1:
        while num < e:
            num = s * (r**(n-1))
            if num > e:
                break
            final.append(num)
            n=n+1
    return final, sum(final)
    