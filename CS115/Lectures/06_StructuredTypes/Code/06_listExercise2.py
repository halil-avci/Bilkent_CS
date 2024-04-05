# -*- coding: utf-8 -*-
"""
@author: CS115
"""
words = []
for i in range(5):
    word = input('Input word: ')
    words.append(word)

print(words)

for i in range(len(words)-1,-1,-1):
    if words[i][0] == words[i][0].upper():
        print(words[i])

shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print('Shortest word: '+shortest)