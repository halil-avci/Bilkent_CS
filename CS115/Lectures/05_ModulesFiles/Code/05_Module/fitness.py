# -*- coding: utf-8 -*-
"""
@author: CS115
"""
MAX_RATE_CONSTANT = 220
MIN_BMI = 21
MAX_BMI = 24

#calculate and return bmi
def calculate_bmi( weight, height ):
    bmi = weight / height **2
    return bmi

#displays bmi category
def display_bmi_category( bmi ):
    if bmi > 30:
        print('Obese')
    elif bmi > 25:
        print('Overweight')
    elif bmi > 20:
        print('Normal weight')
    else:
        print('Underweight')
        
#calculate target heart rate
def calculate_target_heart_rate( age ):
    target = MAX_RATE_CONSTANT - age
    target *= 0.8
    return target

#calculate and display weight range
def display_weight_range( height ):
    min_weight = MIN_BMI * height**2
    max_weight = MAX_BMI * height**2
    print('Your weight should be between:', str(min_weight),'and',str(max_weight))
    return max_weight

    