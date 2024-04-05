# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def separate(ori):

    even = [x for x in ori if x % 2 ==0]
    odd =  [x for x in ori if x % 2 !=0]
    return (even,odd)

L = [1,7,9,2,0,3,7]

ev, od = separate(L)

print(ev)
print(od)