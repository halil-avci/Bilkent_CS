# -*- coding: utf-8 -*-
"""
@author: CS115
"""
table = [[0,3,0],
         [0,0,1],
         [0,0,1],
         [2,0,3],
         [3,1,0],
         [2,5,4]]
print(table)

#
table = []
table.append([0,3,0])
table.append([0,0,1])
table.append([2,0,3])
table.append([3,1,0])
table.append([2,5,4])

#table[1].append(4)

for row in table:
    for col in row:
        print(col,end=" ")
    print() 
print()    
for row in range(len(table)):
    for col in range(len(table[row])):
        print(table[row][col],end=" ")
    print() 
