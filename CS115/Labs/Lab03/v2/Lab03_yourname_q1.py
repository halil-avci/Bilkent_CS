#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:41:09 2021

@author: CS115
"""

def is_neat_reversible(s): 
    """
    Checks whether the input string s is neat reversible. 
    After moving the first char of s to the end, if the reversed 
    result gives the same string as the original, 
    then it is neat reversible, else it isn’t.
    
    Parameters
    ----------
    s (str):    input string

    Returns
    -------
    bool:  True if input string s is neat reversible, False otherwise
    """
    # s needs at least one character to be neat reversible
    if len(s) == 0:
        return False
    # move first char of s to end
    temp_s = s[1:] + s[0]
    # return true if reverse of temp_s is same as original
    return temp_s[::-1] == s

def capitalize_word_at(s, index):
    """
    Creates and returns a string in which the letters in s 
    starting from the input index up to the first space character 
    are capitalized.

    Parameters
    ----------
    s (str):      input string
    index (int):  starting index to capitalize letters

    Returns
    -------
    str:  a new string which is identical to s except letters from 
          the input index up to the first space are capitalized

    """
    space_index = len(s)  # no space
    for i in range(index, len(s)):
        if s[i] == ' ':
            space_index = i
            break
    # capitalize all letters from index up to space_index
    new_s = s[:index] + s[index:space_index].upper() + s[space_index:]
    return new_s

def capitalize_neat_reversibles(s):
    """
    Creates and returns a new string from the input string
    in which all neat reversible words are capitalized.

    Parameters
    ----------
    s (str): input string

    Returns
    -------
    str:    a new string which is identical to s except all neat reversible 
        words are capitalized
    """
    word = ''
    new_s = s
    word_index = 0
    # for each word, check if it is neat reversible, 
    # if so capitalize it using capitalize_word_at() function
    for i in range(len(s)):
        if s[i] != ' ':
            word += s[i]
        if s[i] == " " and s[i + 1] != " ":
            if is_neat_reversible(word):
                new_s = capitalize_word_at(new_s, word_index)
            word = ''
            word_index = i + 1
    # check last word
    if word:
        if is_neat_reversible(word):
            new_s = capitalize_word_at(new_s, word_index)
    return new_s


sentence = input('Enter a sentence: ')
while sentence:    
    print("neat reversibles capitalized:\n", 
          capitalize_neat_reversibles(sentence))        
    sentence = input('Enter a sentence: ')
            
print('bye!')
