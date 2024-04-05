# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:05:41 2021

@author: user
"""
from Cab import *

class Hatchback(Cab):
    __price_per_km = 2.2
    def __init__(self, typo, kms, year):
        Cab.__init__(self, typo, kms, year)
        
    def calculate_Fare(self):
        return self.get_kms() * Hatchback.__price_per_km 