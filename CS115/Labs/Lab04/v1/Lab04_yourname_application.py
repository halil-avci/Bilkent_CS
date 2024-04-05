# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import Lab04_yourname_module as md

md.extract_data('ist_data.txt','ist_districts.txt', 'ist_income.txt')

#get starting district
district = input('Enter district to search (quit to exit): ')
while district.lower() != 'quit':
    dist_income = md.find_income(district, 'ist_income.txt')
    if dist_income != 0:
        print(f'Annual Income for {district}: ${dist_income:.2f}')
    else:
        print(f'{district} not found...')
    #find next district
    district = input('Enter district to search (quit to exit): ')
print('Thank you - Goodbye')