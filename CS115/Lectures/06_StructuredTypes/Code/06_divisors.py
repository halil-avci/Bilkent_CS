# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def findDivisors(n1, n2):
    minVal,maxVal = None, None
    for i in range(2 , min(n1,n2)+1):
        if n1%i == 0 and n2%i==0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

minDivisor, maxDivisor = findDivisors(100,200)
res = findDivisors(5,7)

print("Divisors: ", minDivisor,maxDivisor)
print(res)