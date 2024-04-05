# -*- coding: utf-8 -*-
"""
@author: CS115
"""

#Write a program that reads patients from a file
#Your program will use a dictionary which stores
#doctors and their patient lists.
#Each patient is assigned a doctor.  If the doctor
#already exists, add the patient information to the
#doctors patient list, or add the doctor and patient
#if they do not exist.

def read_doctors( file ):
    doc_dict = {}
    for line in file:
        line = line.split(',')
        line[-1] = line[-1][:-1]
        doc = tuple(line[0:2])
        patient = tuple(line[2:])
        if doc in doc_dict:
            doc_dict[doc].append(patient)
        else:
            doc_dict[doc] = [patient]
    return doc_dict

def display_data( pname, doc_dict ):
    for key in doc_dict:
        for patient in doc_dict[key]:
            if patient[1].lower() == pname.lower():
                print(patient[0],pname,patient[2],'Doctor:',key[1])
file = open('patient_list.txt', 'r')
dict1 = read_doctors(file)
file.close()

for doc in dict1:
    print(doc[1],':',doc[0])
    for patient in dict1[doc]:
        print('\t',patient[0],patient[1],'(',patient[2],')')

#Input the name of a patient and display their doctor.
name = input('Enter patient name to search: ')
display_data( name, dict1 )           