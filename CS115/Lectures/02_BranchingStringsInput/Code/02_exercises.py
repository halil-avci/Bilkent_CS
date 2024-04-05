# -*- coding: ISO-8859-9 -*-
"""
@author: cs115
"""

"""Input a number from the user, and output ‘[number] is divisible by 5 or 7’ 
if the number is divisible by 5 or 7.
"""
num = int(input('Enter number: '))
if num%5 == 0 or num%7 == 0:
    print(num,' is Divisible by 5 or 7')


"""Write a Python program to guess a number between 1 to 9. 
If the user guesses incorrectly display the message, “Wrong Guess!”, 
on successful guess, user will see a "Well guessed!" message.
"""
num = 6
guess = int(input('Enter your guess: '))
if num == guess:
    print('Well guessed!')
else:
    print('Wrong Guess!')


"""Input a word and give an appropriate message if the word has 
the same letter at the beginning and the end of the word or not.
"""
word = input('Enter a word: ')
if word[0] == word[-1]:
    print('Word', word,'begins and ends with same letter')
else:
    print('Word',word,'does not begin and end with same letter')
    
"""Input a user’s height (in metres) and weight (in kgs) and calculate 
his/her BMI and output the BMI category according the following:
      bmi >= 30  		Obese
      25 >= bmi <30  	Overweight
      20 >= bmi <25  	Normal
      bmi < 20 			Underweight
"""
height = float(input('Enter height (meters): '))
weight = int(input('Enter weight (kg): '))
bmi = weight / (height**2)
if bmi >= 30:
    category = 'Obese'
elif bmi >= 25:
    category = 'Overweight'
elif bmi >= 20:
    category = 'Normal Weight'
else:
    category = 'Underweight'

print('With bmi:',bmi,'your category is',category)