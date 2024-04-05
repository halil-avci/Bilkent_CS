# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:04:56 2021

@author: user
"""

def formSentence(inlist, searchChr):
    sentence =''

    for row in inlist:
       for word in row:
    	   if word[0].lower() == searchChr.lower():
              sentence += word + ' '
            
    return sentence

mat = [['This','is','lab','Script'],
       ['We','should','finish','it'],
       ['we','solve','some','questions']]
      
print('Two Dimensional List: ')
for row in mat:
    print(row)
sent = formSentence(mat, 's')
print('Sentence:',sent)