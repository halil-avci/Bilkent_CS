# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:26:29 2020

"""

from Personnel import *
def read_file(fn):
    p_list = []
    
    f = open(fn, 'r')
  
    
    for line in f:     
        parts = line.strip().split(',')
        p = Personnel(parts[0], parts[1], parts[2],  parts[3], float(parts[4]))
        p_list.append(p)
        
  
    f.close()
    return(p_list)
 
    
pL = read_file('personnel.txt')  

for p in pL:
    p.increase_salary()
    
print('All personnel: ')
print(pL)

selected = {}

for p in pL:
    if p.getStatus() == 'B':
        selected[p.getId()] = p
        

print ('Personnel With Both Managerial and Academic Responsibilities:')
for s in selected:
    print(selected[s])

     

    
    
    
    
    
