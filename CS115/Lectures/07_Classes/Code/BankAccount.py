# -*- coding: utf-8 -*-
"""
@author: CS115
"""

class BankAccount:
    def __init__(self,initialBalance, name):
        self.__balance = initialBalance
        self.__customerName = name
        
    def withdraw(self, amount):
        self.__balance -= amount
        
    def deposit(self, amount):
        self.__balance += amount
        
    def getBalance(self):
        return self.__balance
    
    def getCustomerName(self):
        return self.__customerName
    
    def setCustomerName(self, name):
        self.__customerName = name   
    def __str__(self):
        return "Name: "+self.__customerName+"\nBalance: "+str(self.__balance)