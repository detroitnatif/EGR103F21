# -*- coding: utf-8 -*-
"""
[football.py]
[Tyler Klimas]
[9/17/21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [tk206]
"""
# %% Imports
from football_helper import bounded

# %% Define function
def you_shall_pass(pa, pc, py, td, intr):
    rating = 0
    a = bounded(((pc/pa)-.3)*5)
    b = bounded(((py/pa)-3)*.25)
    c = bounded((td/pa)*20)
    d = bounded(2.375 - ((intr/pa)*25))
    num = ((a+b+c+d)/6)*100
    rating += num
    return round(rating, 1)



if __name__ == "__main__":
    print(you_shall_pass(30, 20, 286, 3, 0))
