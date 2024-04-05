#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:58:25 2021

@author: CS115
"""

hour1 = int(input("Enter starting hour: "))
minute1 = int(input("Enter starting minute: "))

hour2 = int(input("Enter ending hour: "))
minute2 = int(input("Enter ending minute: "))

# Assume lunch_time is at least 35 minutes

if hour1 > hour2:
    print('Starting time must be before ending time...')
elif hour1 == hour2:
    if minute2 <= minute1:
        print('Starting time must be before ending time...')
    elif minute2 - minute1 >= 35:
        print('You can have lunch!')
    else:
        print('Not enough time for lunch :(')
elif hour1 == hour2 - 1:
    if 60 + minute2 - minute1 >= 35:
        print('You can have lunch!')
    else:
        print('Not enough time for lunch :(')
else:
    print('You can have lunch!')
