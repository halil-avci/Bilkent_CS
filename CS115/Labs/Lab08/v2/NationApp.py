#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:37:02 2020

@author: user
"""

from Nation import *

def bubble_sort(data):
    issorted = False;
    j = 0
    while(j < len(data)-1 and not issorted):
        issorted = True;
        for k in range(len(data)-j-1):
            if data[k].getContinent() > data[k+1].getContinent():
                issorted = False
                (data[k], data[k + 1]) = (data[k+1], data[k])
            elif data[k].getContinent() == data[k+1].getContinent():
                if data[k].getCountry() > data[k+1].getCountry():
                    issorted = False
                    (data[k], data[k + 1]) = (data[k+1], data[k])
        j = j + 1

def binary_search(data, cName, startInd, endInd):
    if(startInd > endInd):
        return -1
    else:
        mid = (startInd + endInd)//2
        if(data[mid].getCountry() == cName):
            return mid
        elif(data[mid].getCountry()  > cName):
            return binary_search(data, cName, startInd, mid-1)
        else:
            return binary_search(data, cName, mid+1, endInd)

def read_nations(fileName):
    nations = []
    nFile = open(fileName,'r')
    for line in nFile:
        data = line.strip().split(';')
        name = data[0]
        continent = data[1]
        pop = int(data[2])
        area = int(data[3])
        nations.append(Nation(name, continent, pop, area))
    nFile.close()
    return nations

nations = read_nations('nations.txt')
nations.sort()
print('Nations Sorted according to their Names:')
print(nations)

name = input('Enter the name of the country to search: ')

res = binary_search(nations, name, 0, len(nations)-1)

if res != -1:
    print(nations[res])
else:
    print('This country does not exist!')

bubble_sort(nations)
print('Nations Sorted according to their Continent and Name:') 
print(nations)
