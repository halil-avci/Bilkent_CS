# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:49:22 2021

@author: Teacher
"""

def form(s1, s2):
    pos1 = s1.find(s2)
    s3 = ''
    
    #check if the occurrence is found
    if pos1 > -1:
        s3 = s1[:pos1]
        pos2 = s1.rfind(s2)
        s3 += s1[pos2 + len(s2):]
        
    return s3
    
    
    
    
    
str1 = input('Enter first string (exit to quit): ')

while str1.lower() != 'exit':
    str2 = input('Enter second string: ')
    str3 = form(str1, str2)
    print('Formed new string = "' + str3 + '"')
    str1 = input('Enter first string (exit to quit): ')
