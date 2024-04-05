# -*- coding: utf-8 -*-
"""
@author: CS115
"""

#create a range
r1 = range(1,11,2)
for i in r1:
    print(i, end=" ")
print()
#create a range - omit step
for j in range(2,12):
    print(j, end=" ")
print()
#create a range - omit stop and step
for k in range(10):
    print(k,end=" ")
print()

#slicing/indexing ranges
print(range(10)[2:4][1])