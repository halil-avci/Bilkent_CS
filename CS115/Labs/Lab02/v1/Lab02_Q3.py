#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:38:28 2021

@author: CS115
"""

s = input('enter a string (empty to quit): ')

while s:
    part1 = s[:len(s)//2]
    if len(s) % 2 == 0:        
        reverse_part2 = s[len(s):len(s)//2 - 1:-1]        
    else:
        reverse_part2 = s[len(s):len(s)//2:-1]
        
    if part1 == reverse_part2:
        print('It is a mirror string')
    else:
        print('It is NOT a mirror string')           
    s = input('enter a string (empty to quit): ')

print('bye')