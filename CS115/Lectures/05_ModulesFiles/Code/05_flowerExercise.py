# -*- coding: utf-8 -*-
"""
@author: cs115
"""

file1 = open('05_flower1.txt', 'r')
file2 = open('05_flower2.txt', 'r')
outfile = open('05_merged.txt', 'w')
s1 = file1.readline()
s2 = file2.readline()
while s1 and s2:
    if s1 < s2:
        outfile.write(s1)
        s1 = file1.readline()
    else:
        outfile.write(s2)
        s2 = file2.readline()

if s1:
    outfile.write('\n'+s1)
    #get remaining data
    rest = file1.read()
    outfile.write(rest)
else:
    outfile.write('\n'+s2)
    #get remaining data
    rest = file2.read()
    outfile.write(rest)
outfile.close()
file1.close()
file2.close()

    
