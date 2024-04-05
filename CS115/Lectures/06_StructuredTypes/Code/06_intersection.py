# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def intersect( t1, t2):
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

result = intersect((5,'a','b'),(6,'x','b'))
print(result)
