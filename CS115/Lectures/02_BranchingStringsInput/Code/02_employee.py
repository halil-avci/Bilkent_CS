# -*- coding: utf-8 -*-
"""
@author: cs115
"""


hourly_wage=float(input('Enter your hourly wage: '));
hours=int(input('How many hours have you worked? '));

if hours < 40:
    salary=hourly_wage * hours
else:
     salary=40*hourly_wage + (hours-40)*hourly_wage*1.5
     
print('Your salary is: ' + str(salary) + '$');
                
