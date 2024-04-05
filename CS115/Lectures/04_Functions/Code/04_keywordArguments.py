# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ',' + firstName)
    else:
        print(firstName, lastName)

printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', reverse = False)
printName('Olga', lastName = 'Puchmajerova', reverse = False)
printName(lastName = 'Puchmajerova', firstName = 'Olga', reverse = False)

"""
def printName(firstName, lastName, reverse = False):
    if reverse:
        print(lastName + ',' + firstName)
    else:
        print(firstName, lastName)
"""    
printName('Olga', 'Puchmajerova')
printName('Olga', 'Puchmajerova', True)
printName('Olga', lastName = 'Puchmajerova', reverse = True)
