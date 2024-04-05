# -*- coding: utf-8 -*-
"""
@author: CS115
"""
from BankAccount import BankAccount

myAccount = BankAccount(5000,"Jane Doe")
print(myAccount)

myAccount.deposit(1000)
myAccount.withdraw(2000)


