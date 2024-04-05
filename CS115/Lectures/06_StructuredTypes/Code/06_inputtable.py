# -*- coding: utf-8 -*-
"""
@author: CS115
"""
def print_table1(tbl):
    for row in tbl:
        for col in row:
            print(col,end=" ")
        print() 
    print()
def print_table2(tbl):
    for row in range(len(tbl)):
        for col in range(len(tbl[row])):
            print(tbl[row][col],end=" ")
        print() 
    print()
def sum_rows(tbl):
    for r in range(len(tbl)):
        tot=0
        for col in range(len(tbl[r])):
            tot+=tbl[r][col]
        print('Sum of row',r+1,':',tot) 
def sum_cols(tbl):
    for c in range(len(tbl[0])):
        tot=0
        for r in range(len(tbl)):
            tot+=tbl[r][c]
        print('Sum of col',c+1,':',tot) 
        
ROWS=2
COLS=3
table=[]

###OPTION 1
for r in range(ROWS):
    #table.append([])
    row = []
    for val in range(COLS):
        row.append(int(input('Enter value row '+str(r)+' col '+str(val)+': ')))
        #table[r].append(int(input('Enter next value:')))
    table.append(row)
print_table1(table)        
"""
table=[]
###OPTION 2
for r in range(ROWS):
    table.append([])
    
    for val in range(COLS):
        table[r].append(int(input('Enter next value:')))
print_table2(table)
 """
sum_rows(table)
sum_cols(table)