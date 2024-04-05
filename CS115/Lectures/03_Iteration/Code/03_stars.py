# -*- coding: utf-8 -*-
"""
@author: cs115
"""

MAX_ROWS = 10
for row in range(1, MAX_ROWS + 1,1):
    for star in range(1,row + 1,1):
        print ("*", end=' ')
    print()
