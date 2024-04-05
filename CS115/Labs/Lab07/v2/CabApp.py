# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:57:12 2021

@author: User-pc
"""
from Sedan import *
from Hatchback import *

def find_greater(lst, c):
        count = 0
        for car in lst:
            if car > c:
                count += 1
                
        return count
      

def read_file(fn):           
    lst = []
    inp = open('cabs.txt', 'r')
    
    for line in inp:
        parts = line.strip().split(';')
        
        if parts[0] == 'Sedan':
            c = Sedan(parts[0], int(parts[1]), int(parts[2]))
        else:
            c = Hatchback(parts[0], int(parts[1]), int(parts[2]))
   
        lst.append(c) 
    inp.close()
    return lst
        

cabList = read_file('cabs.txt')   

count = 1
for c in (cabList):
    if c.get_type() == 'Sedan':
        print('Sedan', count, 'will pay', c.calculate_Fare(), 'TL')
        count += 1
    
cab1 = Cab('Sedan', 0, 2015)
print('\nThere are', find_greater(cabList, cab1), 'Sedan cars newer than 2015')

cab2 = Cab('Hatchback', 0, 2020)
total = 0
for c in cabList:
    if c == cab2:
        total += c.get_kms()
        

print('\nAll Hatchback cars of year 2020 have travelled',total,'kms')



