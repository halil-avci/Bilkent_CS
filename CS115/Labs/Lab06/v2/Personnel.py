# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:18 2020

"""

class Personnel:
    def __init__(self, id1, name, dept, status, salary):
        self.__id = id1
        self.__name = name
        self.__department = dept
        self.__status = status
        self.__salary = salary     
        
    def getId(self):
        return self.__id
        
    def getName(self):
        return self.__name
    
    def getDepartment(self):
        return self.__department
    
    def getStatus(self):
        return self.__status

    def getSalary(self):
        return self.__salary
    
    def increase_salary(self):
        if self.__status == 'M':
            self.__salary += self.__salary * 0.12
        elif self.__status == 'A':
            self.__salary += self.__salary * 0.15
        else:
            self.__salary += self.__salary * 0.18
            
           
    def __str__(self):
        s = 'Id:' + self.__id + '\n'
        s += 'Department: ' + self.__department + '\n' 
        s += 'Salary: ' + str(self.__salary) + ' TL\n'
        
        return s
        
    def __repr__(self):
        s = 'Id:' + self.__id + '\n'
        s += 'Name:' + self.__name + '\n'
        s += 'Department: ' + self.__department + '\n' 
        s += 'Status:' + self.__status + '\n'
        s += 'Salary: ' + str(self.__salary) + ' TL\n'
        return s
    
        
        
        
        
    
    
