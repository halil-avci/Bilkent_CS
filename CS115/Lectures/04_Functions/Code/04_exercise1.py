# -*- coding: utf-8 -*-
"""
@author: CS115
"""
def digit_sum(n):
    summ = 0
    while (n != 0):
        digit = n % 10
        summ += digit
        n = n // 10
    return summ

num = int(input('Enter a positive integer (<=0 will stop inputting):'))
while( num > 0 ):
    summ = digit_sum(num)
    print( summ )        
    num=int(input('Enter a positive integer (<=0 will stop inputting:'))