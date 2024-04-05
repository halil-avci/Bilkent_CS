#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:42:16 2021

@author: CS115
"""

name1 = input('Enter first name: ')
name2 = input('Enter second name: ')
name3 = input('Enter third name: ')

count = 1
longest = name1

if len(name2) > len(longest):
    longest = name2
    count = 1
elif len(name2) == len(longest):
    count += 1

if len(name3) > len(longest):
    longest = name3
    count = 1
elif len(name3) == len(longest):
    count += 1

print(longest, '\'s name is the longest', end = '')
if count > 1:
    print(', but there is a tie!')
    
