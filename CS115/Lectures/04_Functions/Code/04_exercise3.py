# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def is_binary(s):
    """
    Assumes s is a string
    Returns True if s is a bianry num with 0s and 1s
    Returns False otherwise
    """
    # for every char in s, check if it is 0 or 1
    for ch in s:
        if ch not in '01':
            return False
    
    return True
        

def convert_to_decimal(s):
    """
    Assumes s is a string representing 
    a binary number consisting of 
    only 0s and 1s
    Returns its decimal value
    """
    # for every bit of s in reverse
    decimal = 0
    power = 0
    for bit in s[::-1]:
        decimal += int(bit) * 2 ** power
        power += 1
        
    return decimal


numStr = input('first binary? ')
while numStr:
    if is_binary(numStr):    
        print('decimal of', numStr, 'is', 
                  convert_to_decimal(numStr))
    else:    
          print('Input must be binary') 
    numStr = input('next binary? ')

print('bye')        
        
