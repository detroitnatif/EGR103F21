# -*- coding: utf-8 -*-
"""
[tri_calc.py]
[Tyler Klimas]
[9-19-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
# %% Import modules
import numpy as np
import matplotlib.pyplot as plt
import math

# %% Define function
def triangles(a, b, c, draw=False, fnum=1):
    # %% Calculate angles
    A = math.acos((((a**2) - (b**2) - (c**2))/((-2) * b *c)))
    B = math.acos((((b**2) - (a**2) - (c**2))/((-2) * a *c)))
    C = math.acos((((c**2) - (a**2) - (b**2))/((-2) * a *b)))
    # %% Make plot if asked
    if draw:
        fig = plt.figure(num=fnum, clear=True)
        ax = fig.add_subplot(1, 1, 1)
        plt.plot([0,a],[0,0], '-r')
        plt.plot([a, c*(math.cos(B))], [0, c*(math.sin(B))], '-r')
        plt.plot([c*(math.cos(B)), 0], [c*(math.sin(B)), 0], '-r')

        ax.axis("equal")
        fig.tight_layout()

    # %% Return angles
    return A, B, C


if __name__ == "__main__":
    print(triangles(3, 6, 4, True, 5))