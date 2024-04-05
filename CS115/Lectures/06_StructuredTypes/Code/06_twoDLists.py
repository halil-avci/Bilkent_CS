# -*- coding: utf-8 -*-
"""
@author: CS115
"""


a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
b = a[0]
print(b)
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print(a[0])
print(b)


a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
    
    
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
    

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)

n = 3
m = 4
a = [[0] * m] * n
a[0][0] = 5
print(a[1][0])

n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m

n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)

# the first line of input is the number of rows of the array
n = int(input()) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

# the first line of input is the number of rows of the array
n = int(input()) 
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)

# the first line of input is the number of rows of the array
n = int(input()) 
a = [[int(j) for j in input().split()] for i in range(n)]