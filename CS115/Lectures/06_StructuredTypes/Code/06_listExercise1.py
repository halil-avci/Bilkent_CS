# -*- coding: utf-8 -*-
"""
@author: CS115
"""
values = []
num = int(input('Enter a number (-1 to quit): '))
while num != -1:
    values.append(num)
    num = int(input('Enter a number (-1 to quit): '))

print(values)

limit = int(input('Enter the limit: '))
for i in range(len(values)):
    if values[i] > limit:
        print('Index of first element over',limit,':',i)
        values.pop(i)
        break

        
