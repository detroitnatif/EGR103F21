# -*- coding: utf-8 -*-
"""
Python version of Chapra Figure 4.2
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
@author: DukeEgr93
v. 1.3, 9/21/2019
"""

import math as m


def iter_meth(x, es=0.0001, maxit=50):
    """
    Maclaurin series of exponential function
      fx, ea, it = iter_meth(x, es, maxit)
    input:
      x = value at which series evaluated
      es = stopping criterion (default = 0.0001)
      maxit = maximum iterations (default = 50)
    output:
      fx = estimated value
      ea = approximate relative error (%)
      it = number of iterations
    """

    # initialization
    it = 1
    sol = 1
    ea = 100

    # iterative calculation
    while True:
        solold = sol
        sol = sol + x ** it / m.factorial(it)
        it = it + 1
        if sol != 0:
            ea = abs((sol - solold) / sol) * 100

        if ea <= es or it >= maxit:
            break

    fx = sol

    return fx, ea, it
