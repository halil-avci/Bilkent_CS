# -*- coding: utf-8 -*-
"""
@author: CS115
"""

"""Write a program that converts 400oK to Celsius,  
and displays the result in a proper format.
	T(°C) = T(K) - 273.15
"""
k = 400
c = k - 273.15
print(f'{k:d} Degrees K is {c:.2f} degrees C')

"""Write a program that finds the area and perimeter of a 
circle with the radius 1.5 cm and display the result. 
You can assume pi is the constant value 3.14.
"""
pi = 3.14
r = 1.5
area = pi * r ** 2
perimeter = 2 * r * pi
print(f'Area: {area:.2f} Perimeter: {perimeter:.2f}')

"""Write a program that finds the sum of the first and 
last digit of some number.
"""
num = 3715
first = 3715//1000
last = num%10
sumDigits = first + last
print(f'The sum of {first} and {last:d} is {sumDigits:d}')

"""Write a program to calculate the number of hours and minutes needed 
for a car to travel 500 kilometers at the velocity 110 km/h.
"""
distance = 500
velocity = 110
hours = distance // velocity
minutes = (distance / velocity - hours) * 60

print(f'It will take {hours} hours and {minutes} minutes to travel {distance} kms \
at a speed of {velocity} km/h')
