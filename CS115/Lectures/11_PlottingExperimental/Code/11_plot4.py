# -*- coding: utf-8 -*-
"""
@author: CS115
"""

from matplotlib.pyplot import *
from numpy import *
clf()
x = arange(1,11)
y = x**2


plot(x,y)
xlabel('x')
ylabel('y')
title('y is equal to x squared')
legend(['y = x**2'])