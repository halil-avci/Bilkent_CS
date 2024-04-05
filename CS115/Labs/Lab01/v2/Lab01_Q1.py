#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:38:41 2021

@author: CS115
"""

x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

result = (x + y * z) * (x * y + z) / ( x * y * z)
print(f'f({x}, {y}, {z}) = {result:.2f}')