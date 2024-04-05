# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import matplotlib.pyplot as pl
import numpy as np
x = np.arange(-2,4.1,0.1)
y = 3 * x **3-26 * x + 10
y1 = 9*x**2 - 26
y2 = 18 * x 

pl.clf()
pl.plot(x, y,'r*-' ,x, y1,'bo-',x, y2,'mx-')
pl.legend(['y=3x3 – 26x + 10', 'y1=9x2 – 26', 'y2=18x'])
pl.xlabel('x [-2:4]')
pl.ylabel('y')
pl.title('Plot of Derivative')

pl.grid(True)
