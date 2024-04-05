#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:50:28 2021

@author: CS115
"""

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))


# display the largest even integer and sum of evens
even_sum = 0 
even_max = num1
even_count = 0
if num1 % 2 == 0:
    even_sum += num1
    even_count += 1
if num2 % 2 == 0:
    even_sum += num2
    even_count += 1
    if num2 > even_max:
        even_max = num2
if num3 % 2 == 0:
    even_sum += num3
    even_count += 1
    if num3 > even_max:
        even_max = num3

if even_count > 0:
    print('sum of evens is', even_sum)
    print('even max is', even_max)
else:
    print('No even integer is entered')
    