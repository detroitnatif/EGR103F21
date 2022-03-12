#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:13:15 2021

@author: tylerklimas
"""

def bags(strength, food):
    newarr = []
    item_count = []
    for j in (food):
        item_count.append(0)
    for i in food:
        for k in food:
            if i != k and food[i] == food[k]:
                newarr[i] += food[i]
        
        
    return newarr

bags(1, ['c', 'd', 'c'])
