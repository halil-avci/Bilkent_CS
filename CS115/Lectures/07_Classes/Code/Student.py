# -*- coding: utf-8 -*-
"""
@author: CS115
"""

class Student:
    def __init__(self,name,id):
        self.__id = id
        self.__name = name
        
    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id
    
    def setName(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name
    