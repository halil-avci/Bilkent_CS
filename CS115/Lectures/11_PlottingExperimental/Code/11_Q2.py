# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import matplotlib.pyplot as pl
import numpy as np
import math

x1 = np.arange(-2,1.1,0.1)
x2 = np.arange(-4,4.1,0.1)

y1 = (x1-3)*(x1+2)*(4*x1-0.75)-math.exp(1/2)/2

y2 = (x2-3)*(x2+2)*(4*x2-0.75)-math.exp(1/2)/2
pl.clf()

pl.subplot(2,1,1)
pl.plot(x1, y1)

pl.subplot(2,1,2)
pl.plot(x2, y2)


