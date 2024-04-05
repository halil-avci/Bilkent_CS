# -*- coding: utf-8 -*-
"""
@author: CS115
"""
#try to guess the number picked up by the computer  [0-10] in 3 trials
import random

num = random.randint(1, 10)
 
for k in range (1, 4):
    guess = int(input('Guess the number [1-10]: '))
    if guess == num:
        print('CONGRATULATIONS!')
        break
    else:
        print('Wrong guess!')
    
print('The number was ',num)