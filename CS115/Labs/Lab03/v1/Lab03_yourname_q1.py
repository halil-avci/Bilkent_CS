# -*- coding: utf-8 -*-
"""
CS115
"""

def is_spaced( pwd ):
    """
    takes a password as a parameter and returns True if the space/interval 
    between all digit is not the same.  
    Example: 12345 is not spaced, 34569 is spaced. 
    Hint: you may want to use the ord() function, that returns the integer 
    Unicode value for a given character.

    Parameters:
    pwd (string): password
    
    Returns:
    bool: True if not evenly space, False if evenly spaced

    """
    is_valid = False
    prev = abs( ord(pwd[0]) - ord(pwd[1]))
    for i in range(1,len(pwd) -  1):
        current = abs( ord(pwd[i]) - ord(pwd[i + 1]))
        if prev != current:
            is_valid = True
            break
    return is_valid

def contains_birthyear( pwd, birthyear ):
    """
    takes a password and a birth year as parameters and returns True if the 
    password contains the birth year (in the correct order, with or without 
    characters between) and False if not.
    
    Example:
    contains_birthyear( ‘8657196455’, 1964) -> True
    contains_birthyear( ‘8657159565555455’, 1964) -> True
    contains_birthyear( ‘8965715555554565’, 1964) -> False


    Parameters:
    pwd (string): password
    birthyear(int) : year of user's birth (may also take string)
    
    Returns:
    bool: True password contains birthyear, False if not

    """
    birthyear = str( birthyear )    
    if birthyear in pwd:
        return True
    
    for ch in birthyear:
       pos = pwd.find( ch )
       if pos == -1:
           return False
       pwd = pwd[pos + 1: ]
    return True

def is_valid_password( pwd, year ):
    """
    takes a password and a birthyear as parameters, and using the functions 
    defined in the previous steps returns True if the password passed as a 
    parameter is valid, and False if not.  A password is valid if it meets 
    the following criteria:
    •	Has at least 3 characters.
    •	All characters are numeric
    •	The spacing/interval between adjacent characters is not fixed.
    •	The password does not contain the birth year.


    Parameters:
    pwd (string): password
    birthyear(int) : year of user's birth (may also take string)
    
    Returns:
    bool: True password is valid, False if not

    """
    if len(pwd) < 3 or not pwd.isdigit():
        return False
    if not is_spaced(pwd):
        return False
    if contains_birthyear( pwd, year ):
        return False
    return True

pwd = input('Enter password: ')
year = int(input('Enter year of birth: '))
while not is_valid_password(pwd, year):
    print(f'{pwd} is not a valid password - try again')
    pwd = input('Enter password: ')
    year = int(input('Enter year of birth: '))  
print('Thank you - password is valid')
