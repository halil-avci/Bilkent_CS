# -*- coding: utf-8 -*-
"""
@author: cs115
"""
#
def funa(x):
   #What is the difference between the following statements.
   print(x)
   print(x())

def funb():
    return 50

funa(funb)

def funa(x):
   print(x)

def funb():
    return 50

funa(funb())
