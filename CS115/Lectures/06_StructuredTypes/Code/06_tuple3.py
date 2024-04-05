# -*- coding: utf-8 -*-
"""
@author: CS115
"""
#concatenating tuples
t1 = ( 'a', 'b', 5)
t2 = (7,)
t1 = t1 + t2
print(t1)

#indexing with tuples
print(t1[2])

#slicing tuples
print(t1[1:3])

#repeating tuples
t3 = 2 * t1
print(t3)

#nesting tuples
t4 = ((1,'z'), 8, ('hi', 2, 'u'))
print(t4)