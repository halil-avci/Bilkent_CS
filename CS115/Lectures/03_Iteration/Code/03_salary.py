# -*- coding: utf-8 -*-
"""
@author: CS115
"""
countf = 0
count = 0
sum = 0
for i in range(10):
    status = input("Enter status - (F)ull Time or (P)art Time: ")
    salary = float(input("Enter salary: "))
    if status == "F":
        countf += 1
    count += 1
    sum += salary
average = sum / count

print("There are ",countf," Full Time Instructors")
print("The average salary of all instructors is",average)
    