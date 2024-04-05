#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:56:32 2021

@author: CS115
"""

n = int(input('Enter an int: '))

print(f'Factors of {n}:')
for i in range(1, n): 
        if n % i == 0:
            print(i, ", ", end="")
print(n)