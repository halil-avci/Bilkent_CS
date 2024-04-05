# -*- coding: utf-8 -*-
"""
@author: CS115
"""

#create a dictionary
phone = { 'Evren':7445167,
          'Ana':6413354,
          'Enes':6543210}


name = input('Enter name to search: ')

#find values associated with keys
while name != 'quit':
    if name in phone:
        print(name,"'s contact number is:",phone[name])
    else:
        print(name,' not in dictionary')
    name = input('Enter name to search: ')

#add/update key value pairs
name = input('Enter person to update: ')   
number = input('Enter phone number: ')
if name in phone:
    phone[name] = number
    print(name, 'updated! (', phone[name],')')
else:
    phone[name] = number
    print(name, 'added! (', phone[name],')')
    
#remove keys from dictionary
name = input('Enter person to remove: ')   
if name != 'cancel' and name in phone:
    phone.pop(name)
    print(name, 'removed!')
else:
    print(name, 'not in phone book')

    
#traversing a dictionary
print('Contact List: ')
for people in phone:
    print(people,phone[people])

