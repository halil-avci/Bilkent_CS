# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:24:04 2019

@author: b
"""
from Country import *

def selectionSort(data):
    suffixStart = 0
    while suffixStart != len(data):
        for i in range(suffixStart, len(data)):
            if data[i].getContinent() < data[suffixStart].getContinent():
                data[suffixStart], data[i] = data[i], data[suffixStart]
            elif  data[i].getContinent() == data[suffixStart].getContinent():
                if data[i].getCountry() < data[suffixStart].getCountry():
                    data[suffixStart], data[i] = data[i], data[suffixStart]
        suffixStart += 1

def searchCountries(data, continent, endInd):
    if(endInd == -1):
        return []
    elif data[endInd].getContinent() == continent:
        searchRes = searchCountries(data, continent, endInd-1)
        searchRes.append(data[endInd])
        return searchRes
    else:
        return (searchCountries(data, continent, endInd-1))
    
    
def readCountries(fileName, countries):
    dFile = open(fileName,'r')
    for line in dFile:
        data = line.strip().split(',')
        cName = data[0]
        cContinent = data[1]
        lifeExM = float(data[2])
        lifeExW = float(data[3])
        countries.append(Country(cName, cContinent, lifeExM, lifeExW))
    dFile.close()

countries = []
readCountries('country.txt', countries)


cont = input('Enter continent to search: ')
matches = searchCountries(countries, cont, len(countries)-1)

if len(matches) != 0:
    print('List of Countries in',cont)
    for con in matches:
        print(con)
else:
    print('No countries in', cont)



countryInfo = input('Enter county name, continent, life expectany for Men and life expectany for Women: ')
info = countryInfo.strip().split(',')
newCo = Country(info[0].strip(),info[1].strip(),float(info[2].strip()),float(info[3].strip()))
if newCo not in countries:
    countries.append(newCo)
    print('New Country added')
else:
    print('This Country exists!')

selectionSort(countries)
print('\nCountries by Continent and Name:') 
print(countries)