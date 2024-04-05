# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import numpy as np

#create a one-dimensional array using arange
oneD = np.arange(2,20,3)

#display
print(oneD)

v1 = oneD * 3
print(v1)

v2 = oneD + 6
print(v2)

v3 = oneD ** 2
print(v3)

v4 = oneD - 8
print(v4)

v5 = oneD / 2
print(v5)

#integer division - truncates result
v6 = oneD // 2
print(v6)
