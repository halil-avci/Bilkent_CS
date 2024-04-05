# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def f():
    x = 1
    print(x)
x = 5
f()
print(x)

def g() :
    global x 
    x = 1
    print(x)
 
x = 5
g()
print(x)

