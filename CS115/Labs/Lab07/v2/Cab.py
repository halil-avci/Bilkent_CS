# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:04:11 2021

@author: user
"""

class Cab:
    def __init__(self, ty, kms,year):
        self.__typeOfCab = ty
        self.__kms = kms
        self.__year = year
        
    def get_kms(self):
        return self.__kms
    
    def get_type(self):
        return self.__typeOfCab
    
    def get_year(self):
        return self.__year
    
    def __gt__(self, other):
        if self.__typeOfCab == other.__typeOfCab:
            return self.__year > other.__year
        else:
            return False
    
    def __eq__(self, other):
        return self.__typeOfCab == other.__typeOfCab and self.__year == other.__year
        
    def __repr__(self):
        s = self.__typeOfCab + '\t' + str(self.__kms) + str(self.__year) + '\n'
        return s