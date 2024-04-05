# -*- coding: utf-8 -*-
"""
@author: cs115
"""

MAX_ROWS = 10
    
for row in range(1, MAX_ROWS+1):
    for spaces in range(1, (MAX_ROWS - row)+1):
        print (" ", end='')
    for stars in range(1, 2*row):
        print ("*", end='')
    print()
