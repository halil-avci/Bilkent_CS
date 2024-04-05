# -*- coding: utf-8 -*-
"""
@author: cs115
"""
city = input('Enter city to search: ')
file = open('05_hotels.txt', 'r')
output = open(city+'hotels.txt', 'w' )
for hotel in file:
    pos = hotel.find(city)
    if pos == 0:
        #find the dash
        pos = hotel.find('-')+1
        output.write(hotel[pos:len(hotel)])
file.close()
output.close()