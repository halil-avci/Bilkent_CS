# -*- coding: utf-8 -*-
"""
@author: CS115
"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def fact(n):
    factorial = 1 
    for i in range(1,n+1):
        factorial *= i
    return factorial

L = [1,-2,3.33]
print('L = ', L)
print('Apply abs to each element of L')
applyToEach(L, abs)
print('L = ', L)

print('Apply int to each element of L')
applyToEach(L, int)
print('L = ', L)

print('Apply factorial to each element of L')
applyToEach(L, fact)
print('L = ', L)

#ALTERNATIVE SOLUTION - LIST COMPREHENSIONS
L = [5,7,4]
print('L = ', L)
L2 = [ fact(x) for x in L]
print('L2= ', L2)

