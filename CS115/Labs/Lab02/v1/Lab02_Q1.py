#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:16:21 2021

@author: CS115
"""

"""
Note to TAs & Tutors:
    Students should NOT use break in this question.
    Although it is not wrong to do so, it is more informative 
    to have a loop condition which indicates when to stop.
"""    

import random

target_total = 1000

# generate a random int between 1 and 20, inclusive
num = random.randint(1, 20)

total = 0
count = 1
while total <= target_total and count <= 100 :
    total += num
    # generate a new random int in [1..20]
    num = random.randint(1, 20)
    count += 1
    
print('Sum of', count, 'random ints in [1..20] is', total)    



