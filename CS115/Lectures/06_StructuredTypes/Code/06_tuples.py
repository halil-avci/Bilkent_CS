# -*- coding: utf-8 -*-
"""
@author: CS115
"""

#create an empty tuple
t1 = ()

#create a tuple containing 3 values
t2 = (1,"Two", 3)

#display the tuples
print(t1)
print(t2)

#display an element in a tuple
print( t2[1] )

#display the type of the element
print( type(t2[1]))
 
#tuples are immutable
t2[0] = 5
