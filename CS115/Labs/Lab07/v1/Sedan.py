# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:04:41 2021

@author: user
"""
from Cab import *

class Sedan(Cab):
    __price_per_km = 2
    def __init__(self, typo, kms):
        Cab.__init__(self, typo, kms)
        
    def calculate_Fare(self):
        return self.get_kms() * Sedan.__price_per_km