# -*- coding: utf-8 -*-
"""
@author: CS115
"""

#try to guess the number picked up by the computer  [0-10] in 3 trials
import random

num = random.randint(1, 10)
guess = int(input('Guess the number [1-10]: '))
guesses = 1

while guess != num:
    print('Wrong guess!')
    guess = int(input('Guess the number [1-10]: '))
    guesses = guesses + 1
    
print('Congratulations, you guessed in',guesses,'guesses')