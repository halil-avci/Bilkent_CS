# -*- coding: utf-8 -*-
"""
@author: CS115
"""
#creating an empty list
a_list = [] 

#creating a list and initializing values
L = [2,8,3,6] 

#displaying a list
print(L)

#display the number of elements in a list
print(len(L))

#indexing from zero - accessing an element
print(L[0])
print(L[2]+1)
print(L[3])
#print(L[4]) -> no element at index 4

#indexing with variables
i = 2 
L[i-1]

#updating an element
L[1]= 12
print(L)