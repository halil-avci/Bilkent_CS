# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:12:07 2019

@author: user
"""

import numpy as np

x1 = np.array([1,2,3])
x2 = np.array([4,5,6])

x3 = np.array([[1,1,1],[2,2,2]])
x4 = np.array([[3,3,3],[4,4,4]])

c1 = np.concatenate([x1,x2])
print('c1\n',c1)

c2 = np.concatenate([x3,x4])
print('c2\n',c2)

c3 = np.concatenate([x3,x4], axis = 1)
print('c3\n',c3)

c4 = np.vstack([x3,x4])
print('c4\n',c4)

c5 = np.hstack([x3,x4])
print('c5\n',c5)

c6 = np.concatenate([x3,c5], axis = 1)
print('c6\n',c6)

c7 = np.hstack([x3,c5])
print('c7\n',c7)

c8 = np.vstack([x3,x1])
print('c8\n',c8)

#Does not work!  Concatenate can only join arrays
#with same number of dimensions
c9 = np.concatenate([x3,x1])
print('c9\n',c9)