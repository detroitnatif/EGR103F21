# -*- coding: utf-8 -*-
"""
[bounded]
[Tyler Klimas]
[9-11-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [Tk206]
"""


def bounded(x, low=0, high=2.375):
    if x <= 0:
        return 0
    if 0 < x < 2.375:
        return x
    if x >= 2.375:
        return 2.375

