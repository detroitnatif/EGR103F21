# -*- coding: utf-8 -*-
"""
Extended python version of Chapra Figure 4.2
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
@author: DukeEgr93
v. 1.1, 1/21/2021
"""

import math as m
import numpy as np


def iter_meth_ext(x, es=0.0001, maxit=50):
    """
    Maclaurin series of exponential function
      fx, ea, it, sollist, ealist = iter_meth(x, es, maxit)
    input:
      x = value at which series evaluated
      es = stopping criterion (default = 0.0001)
      maxit = maximum iterations (default = 50)
    output:
      fx = estimated value
      ea = approximate relative error (%)
      it = number of iterations
      sollist = estimated values at each iteration
      ealist = approcimate relative error (%) at each iteration
    """

    # initialization
    it = 1
    sol = 1
    ea = 100
    sollist = [sol]
    ealist = [ea]

    # iterative calculation
    while True:
        solold = sol
        sol = sol + x ** it / m.factorial(it)
        it = it + 1
        if sol != 0:
            ea = abs((sol - solold) / sol) * 100

        sollist += [sol]
        ealist += [ea]

        if ea <= es or it >= maxit:
            break

    fx = sol

    return fx, ea, it, np.array(sollist), np.array(ealist)
