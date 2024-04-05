# -*- coding: utf-8 -*-
"""
@author: CS115
"""
population = float( input("Enter initial population: "))
hours = 0
while population <= 1000000:
    hours += 10
    population *= 2 

days = hours // 24
hours = hours % 24
print(f'It will take {days} days and {hours} hours for the population \
to exceed 1 million')