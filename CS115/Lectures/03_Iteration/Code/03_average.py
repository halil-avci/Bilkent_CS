# -*- coding: utf-8 -*-
"""
@author: CS115
"""
sum = 0
count = 0

val = int( input( "Enter an integer (negative or zero to quit): "))
while val > 0:
    count += 1
    sum += val
    val = int( input( "Enter an integer (negative or zero to quit): "))

if count > 0:
    average = sum / count
    print("Average:", average)
else:
    print( "No values input ")
    