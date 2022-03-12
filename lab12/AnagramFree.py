#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:20:11 2021

@author: tylerklimas
"""

words = ["creation","sentence","reaction","sneak","star","rats","snake"]
def getMaximumSubset(words):
    newarr = []
    for i in words:
        newarr.append(sorted(i))

    newarr2 =[]
    for j in newarr:
        newarr2.append(str(j))
    l = sorted(set(newarr2))
    final = []
    for h in range(len(l)):
        final.append(0)
    
    for idx, ele in enumerate(l):
        for ide, el in enumerate(newarr2):
            if ele == el:
                final[idx] += 1

    
       
    fin = len(words)
    return len(l)

                
            



       
    