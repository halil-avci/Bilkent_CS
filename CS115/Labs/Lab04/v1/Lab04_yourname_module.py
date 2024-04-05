# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def extract_data( inname1, inname2, outname ):
    """
    Reads the district data from the first input file and the district name
    from the second input file.  Writes the district name and the (average)
    annual income for each district to the output file with the name given.

    Parameters:
    inname1 (string): name of file containing income data
    inname2 (string): name of file containing district data
    outpame (string): name of output file
    
    Returns:
    NoneType: None

    """

    infile1 = open(inname1, 'r')
    infile2 = open(inname2, 'r')
    
    outfile = open(outname, 'w')
    
    #for all lines in the income file
    for line in infile1:
        #read read district from city file
        district = infile2.readline()
        #trim the trailing whitespace if any - careful not all lines have newline
        district = district.strip()
        
        #find the income (last field in each line)
        i_pos = line.rfind('(')
        income = line[i_pos + 1:-3]
        income = income.replace(',','')
        outfile.write(f'{district}\t{income}\n')
    outfile.close()
    infile1.close()
    infile2.close()


def find_income( dist_name, inname ):
    """
    Reads the lines from the input file and from each line extracts the district
    name and income.  Finds and returns the annual income
    for the district with the matching name. Returns 0.0 if no district found. 

    Parameters:
    dist_name(string): name of the district to search
    inname (string): name of file containing district/annual income data
    
    Returns:
    float: annual income (0.0 if district not found)

    """
    
    income = 0
    infile = open( inname )
    for line in infile:
        d_pos = line.find('\t')
        if line[0:d_pos].lower() == dist_name.lower():
            income = float(line[d_pos + 1:])
            break
    infile.close()
    return income


