# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import numpy as np

#create a two-dimensional array using arange
twoD = np.array([[2,3,7,6],[9,5,1,12],[2,6,11,8]])

#display
print(twoD)
print()

v1 = twoD * 3
print(v1)
print()

v2 = twoD + 6
print(v2)
print()

v3 = twoD ** 2
print(v3)
print()

v4 = twoD - 8
print(v4)
print()

v5 = twoD / 2
print(v5)
print()

#integer division - truncates result
v6 = twoD // 2
print(v6)
