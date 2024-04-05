# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def reverse_num(n):
    reverse = 0
    
    while (n != 0):
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse

num=int(input('Enter a positive integer: '))
reverse = reverse_num(num)
print(reverse)        
