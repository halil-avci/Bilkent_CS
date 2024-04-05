# -*- coding: utf-8 -*-
"""
@author: cs115
"""

grade=float(input('Enter your grade: '))
if grade > 100 or grade < 0:
    print('Value out of range')
elif grade>90:
     print('A')
elif grade>80:
     print('B')
elif grade>70:
     print('C')
elif grade>60:
     print('D')
else:
     print('F');     

print('Done')


    