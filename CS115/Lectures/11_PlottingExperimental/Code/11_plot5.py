# -*- coding: utf-8 -*-
"""
@author: CS115
"""

from matplotlib.pyplot import *
from numpy import *

clf()
x = arange(1,11)
y = x**2

subplot(2,1,1)
plot(x,y,'r:*')
xlabel('x')
ylabel('y')
title('y is equal to x squared')
legend(['y = x**2'])


subplot(2,1,2)
plot(x,y,'k-.>')
xlabel('x')
ylabel('y')
title('y is equal to x squared')
legend(['y = x**2'])
grid('on')

