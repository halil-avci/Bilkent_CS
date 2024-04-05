# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:18 2020

"""

class Nation:
    def __init__(self, cName, continent, pop,sa):
        self.__country = cName
        self.__continent = continent
        self.__population = pop
        self.__surface_area = sa
        self.__density = self.calculate_density()
        
    def getCountry(self):
        return self.__country
        
    def getContinent(self):
        return self.__continent
    
    def getPopulation(self):
        return self.__population
    
    def getSurface_area(self):
        return self.__surface_area
    
    def getDensity(self):
        return self.__density
      
    def __str__(self):
        s = 'Country: ' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n' 
        s += 'Density: ' + str(self.__density) + '\n'
        
        return s
    
    def __repr__(self):
        s = 'Country: ' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n' 
        s += 'Population: ' + str(self.__population) + '\n'
        s += 'Area: ' + str(self.__surface_area) + '\n'
        s += 'Density: ' + str(self.__density) + '\n'
        
        return s
    
    def calculate_density(self):
        den = self.__population / self.__surface_area
        return den
    
    def __lt__(self, other):
        return self.__country < other.__country
        
    
        
        
        
        
        
    
    