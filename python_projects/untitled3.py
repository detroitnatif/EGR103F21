#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:19:13 2021

@author: tylerklimas
"""

def score(word):
    length = (len(word))**2
    return length



if __name__ == '__main__':
    print(score('dog'))
    print(score('I'))
    print(score('ox'))
