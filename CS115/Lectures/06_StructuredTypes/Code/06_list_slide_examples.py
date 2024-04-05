# -*- coding: utf-8 -*-
"""
@author: CS115
"""


friends = ['Harry', 'Emily', 'Bob', 'Jane']
friends.pop(1)
print(friends)  

#['Harry', 'Bob', 'Jane'] 
	
friends = ['Harry', 'Emily', 'Bob', 'Jane']
friends.pop()
print(friends)  
#Output:
#['Harry', 'Emily', 'Bob'] 	
	
#Example:
friends = ['Harry', 'Emily', 'Bob', 'Jane']
friends.remove('Bob')
print(friends)  
#Output:
#['Harry', 'Emily',  'Jane'] 