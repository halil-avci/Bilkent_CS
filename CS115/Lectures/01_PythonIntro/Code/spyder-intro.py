#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:43:24 2018

@author: a
"""

pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment (evrything after # symbol)
area = pi * (radius ** 2)
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi * (radius ** 2)
print(area)


#####################################
## COMMENTING LINES
#####################################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!

#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#####################################
## AUTOCOMPLETE
#####################################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1
# use autocomplete to write a line that prints the value of that long variable
# notice that Spyder also automatically adds the closed parentheses for you!

#####################################
## Quick Check 1
#####################################

x = 12 / 5
print(x)

x = 12 // 5
print(x)

x = 10 / 4.0
print(x)

x = 10 // 4.0
print(x)

x = 4 / 10
print(x)

x = 4 // 10
print(x)

x = 12 % 3
print(x)

x = 10 % 3
print(x)

x = 3 % 10
print(x)