# -*- coding: utf-8 -*-
"""
@author: cs115
"""

file1=open('05_worldpop.txt' ,'r')
file2=open('05_worldarea.txt' ,'r')
file3=open('05_world_pop_density.txt' ,'w')

for line1 in file1:
    line2=file2.readline()
    #get numeric values
    pos1=line1.find(' ')
    pos2=line2.find(' ')
    #get population
    pop=float(line1[pos1+1:len(line1)])
    
     #get area
    area=float(line2[pos2+1:len(line2)])
    
     #calculate density
    density=pop/area
    
     #write to the output file
    country=line1[0:pos1]
    file3.write(country+' '+str(density)+'\n')
file1.close()
file2.close()
file3.close()