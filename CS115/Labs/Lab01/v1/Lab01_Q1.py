#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:21:58 2021

@author: CS115
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
x = float(input("Enter x: "))

y = a * x ** 2 + b * x + c
print()
print(f'f( x ) = {a} * x ** 2 + {b} * x + {c}')
print("f(", x, ") = ", f'{y:.2f}')


