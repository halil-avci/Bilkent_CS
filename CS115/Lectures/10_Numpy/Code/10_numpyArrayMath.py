# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

# Elementwise difference
print('Negative:\n',-x)
print(np.negative(x))

# Elementwise sum
print('Add:\n',x + y)
print(np.add(x, y))

# Elementwise difference
print('Subtract:\n',x - y)
print(np.subtract(x, y))

# Elementwise product
print('Multiply:\n',x * y)
print(np.multiply(x, y))

# Elementwise division
print('Divide:\n',x / y)
print(np.divide(x, y))

# Elementwise floor division
print('Floor Division:\n',x // y)
print(np.floor_divide(x, y))

# Elementwise exponentiation 
print('Modulus / Remainder:\n',y % x)
print(np.mod(y, x))

# Elementwise exponentiation 
print('Power:\n',x ** 2)
print(np.power(x, 2))

# Elementwise square root
print('Square Root:\n',np.sqrt(x))