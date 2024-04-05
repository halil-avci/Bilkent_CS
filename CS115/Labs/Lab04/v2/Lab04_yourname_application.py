# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import Lab04_yourname_module as md

city = input('Enter city to search ("quit" to exit): ')
while city.lower() != 'quit':
    found_city = md.district_density(city, 'city_districts.txt','city_values.txt', city.lower()+'_density.txt')
    
    if found_city:
        sdensity = float(input('Enter maximum density: '))
        districts = md.find_districts(sdensity, city.lower()+'_density.txt')
        
        #if districts is not an empty string
        if districts:
            print(f'Districts in {city} with population density below {sdensity}:')
            print( districts )
        else:
            print(f'No districts in {city} with population density below {sdensity}')
            
    else:
        print( city,'not found...' )
    
    
    city = input('Enter city to search ("quit" to exit): ')
    
print('Thank you - Goodbye')