# -*- coding: utf-8 -*-
"""
@author: cs115
"""
#slide 28
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

#slide 28
def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)

#slide 24
def h(y):
    x += 1

x = 5
h(x)
print(x)