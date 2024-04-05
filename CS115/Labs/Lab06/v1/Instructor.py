# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:18 2020

"""

class Instructor:
    def __init__(self, id1, name, status, hours):
        self.__id = id1
        self.__name = name
        self.__status = status
        self.__hours = hours     
        
      
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def getStatus(self):
        return self.__status

    def getHours(self):
        return self.__hours
    
    def calculate_salary(self):
        if self.__status == 'F':
            salary = 5000 + self.__hours * 500
        else:
            salary = self.__hours * 400
        return salary
            
           
    def __str__(self):
        s = 'Name:' + self.__name + '\n'
        s += 'Status: ' + self.__status + '\n' 
        s += 'Salary: ' + str(self.calculate_salary()) + ' TL\n'
        
        return s
        
    def __repr__(self):
        s = 'Id:' + self.__id + '\n'
        s += 'Name:' + self.__name + '\n'
        s += 'Salary: ' + str(self.calculate_salary()) + ' TL\n'
        return s
    
        
        
        
        
    
    
