# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:57:12 2021

@author: User-pc
"""
from Sedan import *
from Hatchback import *

def find_equal(lst, c):
    count = 0
    for car in lst:
        if car == c:
            count += 1
    return count

def read_file(fn):           
    lst = []
    inp = open('cabs.txt', 'r')
    
    for line in inp:
        parts = line.strip().split(':')
        
        if parts[0] == 'Sedan':
            c = Sedan(parts[0], int(parts[1]))
        else:
            c = Hatchback(parts[0], int(parts[1]))
        
        lst.append(c) 
    inp.close()
    return lst
        
    
totalFare = 0

cabList = read_file('cabs.txt')   

sList = []
hList = []
for c in (cabList):
    if c.get_type() == 'Sedan':
        sList.append(c.get_kms())
    else:
        hList.append(c.get_kms())
    totalFare += c.calculate_Fare()
    
print('---Kilometers driven for each cab---')
print('Hatchback:', sum(hList), 'kilometers')
print('Sedan:', sum(sList), 'kilometers')

print('\nTotal number of kilometers driven by all Cabs:',sum(hList) + sum(sList))
   
print('Total Fare Earned from all cabs (in dollars):', totalFare)  

print('\nSorted Cabs:')
cabList.sort()
print(cabList)

cab = Cab('Sedan', 200)
print('\nThere are', find_equal(cabList, cab),'Sedan cabs with 200 kms.')



