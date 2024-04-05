# -*- coding: utf-8 -*-
"""
@author: CS115
"""

from numpy import *

x = array([22,41,58,33,17,32])
r1 = x > 40
print(r1)

r2 = x[x > 40]
print(r2)

r3 = where(x > 40)
print(r3)
