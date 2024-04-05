# -*- coding: utf-8 -*-
"""
@author: CS115
"""
initial = float( input("Enter initial investment: "))
balance = initial
years = 0

while balance < 2 * initial:
    years += 1
    balance += balance * 0.15 
    
print(f'It will take {years} years to double your investment')