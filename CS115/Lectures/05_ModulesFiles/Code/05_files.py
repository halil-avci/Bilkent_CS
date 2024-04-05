# -*- coding: utf-8 -*-
"""
@author: cs115
"""
#writing data to a file
fileHandle = open( '05_file1.txt', 'w')
for i in range(2):
    name = input('Enter name: ')
    fileHandle.write( name+'\n')
fileHandle.close()

#append data to end of  file
fileHandle = open( '05_file1.txt', 'a')
fileHandle.write('Jane Doe\n')
fileHandle.close()

#reading data from a file - read()
fileHandle = open( '05_file1.txt', 'r')
fileContents = fileHandle.read()
print(fileContents)
fileHandle.close()

#reading specific lines from a file - readline()
fileHandle = open( '05_file1.txt', 'r')
for i in range(2) :
    line = fileHandle.readline()
    print(line[:-1])
fileHandle.close()

#read all lines from the file
fileHandle = open( '05_file1.txt', 'r')
for line in fileHandle:
    print(line[:-1])
fileHandle.close()
