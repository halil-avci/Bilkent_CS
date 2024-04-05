#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:33:39 2021

@author: CS115
"""

s = input('Enter a string: ')
while s:
    odds = ''
    evens = ''
    for i in range(len(s)):
        if i % 2 == 0:
            evens += s[i]
        else:
            odds += s[i]
    print('new string is', evens + odds )
    s = input('Enter a string: ')

print('done!')