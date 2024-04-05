#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:08:06 2021

@author: CS115
"""

import random

desired_sum = int(input('Desired dice sum: '))
while desired_sum < 0 or desired_sum == 1 or desired_sum > 12:
    print('Invalid dice sum, try again...')
    desired_sum = int(input('Desired dice sum: '))
    
while desired_sum != 0:
    die1 = 0
    die2 = 0
    count = 0
    while die1 + die2  != desired_sum:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        count += 1
        
    print(count, 'rolls')    
    desired_sum = int(input('Desired dice sum: '))
    while desired_sum < 0 or desired_sum == 1 or desired_sum > 12:
        print('Invalid dice sum, try again...')
        desired_sum = int(input('Desired dice sum: '))
        
print('bye!')        
