#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:50:28 2021

@author: CS115
"""

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))


# count how many of three int inputs are odd
count = 0
if num1 % 2 != 0:
    count += 1
if num2 % 2 != 0:
    count += 1
if num3 % 2 != 0:
    count += 1
print(count, "of the 3 numbers are odd.")