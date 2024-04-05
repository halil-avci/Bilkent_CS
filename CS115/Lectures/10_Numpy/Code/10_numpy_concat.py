# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import numpy as np

#x = np.array([1,2,3])
#y = np.array([3,2,1])
##print(np.concatenate([x,y]))
#
#print()
#z = [99, 99, 99]        
#print(np.concatenate([x, y, z]))
# 
#print()
#grid = np.array([[1, 2, 3],[4, 5, 6]])
#print(np.concatenate([grid, grid])) #default axis = 0
#
#
#print()
#
#
#grid = np.array([[1, 2, 3],[4, 5, 6]])
#print(np.concatenate([grid, grid], axis = 1))


x = np.array([1, 2, 3])        
grid = np.array([[9, 8, 7],                         
                 [6, 5, 4]])

# vertically stack the arrays        
print(np.vstack([x, grid]))

print()
print()

y = np.array([[99],[99]])        
print(np.hstack([grid, y]))
















