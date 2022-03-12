#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:51:59 2021

@author: tylerklimas
"""
import math 
def volume(radius, height):
    vol = 1/3*math.pi*radius**2*height
    return vol 


if __name__ == '__main__':
    print(volume(10, 10))
    print(volume(1, 1))

