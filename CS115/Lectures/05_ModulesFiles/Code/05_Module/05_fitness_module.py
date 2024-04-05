# -*- coding: utf-8 -*-
"""
@author: cs115
"""
from fitness import *

weight = float(input('Enter your weight (in kg): '))
height = float(input('Enter your height (in meters): '))
age = int(input('Enter your age: '))

#calculate and display bmi
bmi = calculate_bmi( weight, height)

print(f'Your bmi is: {bmi:.2f}')

#display the bmi category
display_bmi_category(bmi)

#display target weight range
max = display_weight_range( height )
diff = weight - max
if diff > 0:
    print('You should lose ', diff, 'kgs to reach your target weight')
else:
    print('You do not have excess weight')

#display target heart rate
target_hr = calculate_target_heart_rate(age)
print('Your target heart rate is ', target_hr)
    