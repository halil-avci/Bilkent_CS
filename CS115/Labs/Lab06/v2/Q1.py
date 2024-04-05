# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def formEqualLength(words, n):
    sentence =''

    for c in range (len(words[0])):
       for r in range (len(words)):
    	   if len(words[r][c]) == n:
              sentence += words[r][c] + ' '
            
    return sentence

mat = [['This','is','lab','Script'],
       ['We','should','finish','it'],
       ['we','solve','some','questions']]
      
print('Two Dimensional List: ')
for row in mat:
    print(row)
sent = formEqualLength(mat, 6)
print('Sentence:',sent)

