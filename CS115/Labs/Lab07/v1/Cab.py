# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:04:11 2021

@author: user
"""

class Cab:
    def __init__(self, ty, kms):
        self.__typeOfCab = ty
        self.__kms = kms
        
    def get_kms(self):
        return self.__kms
    
    def get_type(self):
        return self.__typeOfCab
    
    def __lt__(self, other):
        return self.__kms < other.__kms
    
    def __eq__(self, other):
        return self.__typeOfCab == other.__typeOfCab and self.__kms == other.__kms
    
    
    def __repr__(self):
        s = self.__typeOfCab + '\t' + str(self.__kms) + '\n'
        return s