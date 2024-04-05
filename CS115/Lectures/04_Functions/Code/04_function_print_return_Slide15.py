# -*- coding: utf-8 -*-
"""
@author: cs115
"""

def is_even_one(val):
    if val % 2 == 0:
        print('number is even')
    else:
        print('number is odd')
        
def is_even_two(val):
    if val % 2 == 0:
        return True

r1 = is_even_one(4)
print('Value: ', r1, 'Type: ', type(r1))

r2 = is_even_two(4)
print('Value: ', r2, 'Type: ', type(r2))

r3 = is_even_two(5)
print('Value: ', r3, 'Type: ', type(r3))
