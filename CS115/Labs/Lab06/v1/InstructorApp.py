# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:26:29 2020

"""

from Instructor import *
def read_file(fn):
    d = {}
    
    f = open(fn, 'r')
  
    
    for line in f:     
        parts = line.strip().split(';')
        n = Instructor(parts[0], parts[1], parts[2], float(parts[3]))
        d[parts[0]] = n
        
  
    f.close()
    return(d)
 
    
d = read_file('instructor.txt')    
id1 = input('Enter instructor id: ')
try:
    print(d[id1])
except:
    print('No such an Instructor exists!')

selected = []

status = input('Enter status (F - Full-time / P) - Part-time: ')

for c in d:
    if d[c].getStatus() == status:
        selected.append(d[c])


if status == 'F':
    print ('Full-time Instructors:')
else:
    print ('Part-time Instructors:')
print(selected)

     

    
    
    
    
    
