# -*- coding: utf-8 -*-
"""
@author: CS115
"""

#def replace_words(table1, word):
#    for row in range(len(table1)):
#        for col in range(len(table1[row])):
#            if table1[row][col] == word:
#                table1[row][col]= "*"

def replace_words(table1, word):
    for row in table1:
        for col in row:
            if col == word:
                col= "*"
                

wordList = [['apple', 'banana', 'orange'],
            ['banana', 'pear', 'cherry'],
            ['grape', 'pineapple', 'banana']]
word = 'banana'

replace_words(wordList, word)
for row in wordList:
    print( row )
#print(wordList)