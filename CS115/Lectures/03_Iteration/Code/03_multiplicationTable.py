# -*- coding: utf-8 -*-
"""
@author: CS115
"""

print(" "*15,"Multiplication Table")
#Display the number title
print("      ", end="")
for i in range(1,10) :
    print("   " + str(i), end=" ")
print("-"*60)

#Print table body
for i in range(1,10) :
    print(str(i) + " | ", end="  ")
    for j in range(1,10) :
        #Display the product and align properly
        if i*j <= 9:
            print(3*" " + str(i * j), end=" ")
        else :
            print(2*" " + str(i * j), end=" ")
    print()


