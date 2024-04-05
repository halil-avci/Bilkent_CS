#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:37:38 2021

@author: CS115
"""

n1 = int(input('enter first int > 0 [0 to quit]: '))

while n1 < 0:
    print('You must enter a positive int, try again....')
    n1 = int(input('enter first int > 0 [0 to quit]: '))

n2 = int(input('enter second int > 0 [0 to quit]: '))
while n2 < 0:
    print('You must enter a positive int, try again....')
    n2 = int(input('enter second int > 0 [0 to quit]: '))

if n2 < n1:
    n1, n2 = n2, n1

# find all pretty numbersin [n1, n2]
for num in range(n1, n2 + 1):
    total = 0
    num_digits = len(str(num))
    for d in str(num):
        total += int(d) ** num_digits
    if total == num:
        print(num, 'is  a pretty number')
        
        
        
        
        