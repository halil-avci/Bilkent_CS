# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def union( t1, t2):
    result = t1
    for e in t2:
        if e not in result:
            result += (e,)
    return result

result = union((5,'a','b'),(6,'x','b'))
print(result)
