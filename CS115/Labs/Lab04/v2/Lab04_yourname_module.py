# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def district_density( scity, inname1, inname2, outname ):
    """
    Reads the city and district names from the first input file and the population
    density data from the second input file.  Writes to the output file the 
    calculated population density (population / area) for each district in the 
    city with the given name.
    
    Parameters:
    city (string): name of the city to search
    inname1 (string): name of file containing city/district data
    inname2 (string): name of file containing population data
    outpame (string): name of output file
    
    Returns:
    bool: True if the city exists in the file, False if not
    """

    infile1 = open(inname1, 'r')
    infile2 = open(inname2, 'r')
    
    outfile = open(outname, 'w')
    
    #read and discard the header line from each input file
    infile1.readline()
    infile2.readline()
    
    found = False
      
    #for all lines in the city file
    for line in infile1:
        #read read data from population file
        data = infile2.readline()
        #trim the trailing whitespace if any - careful not all lines have newline
        data = data.strip()
        
        #find the city name
        c_pos = line.find('\t')
        city = line[0:c_pos]
        
        if city.lower() == scity.lower():
            #city was found
            found = True
            
            #get district
            district = line[c_pos+1:].strip()
            
            #find the population and area
            p_pos = data.rfind('\t')
            population = data[0:p_pos]
            population = float(population.replace(',',''))
            area = float(data[p_pos + 1:].strip().replace(',',''))
            density = population / area
            outfile.write(f'{district},{density:.1f}\n')
    outfile.close()
    infile1.close()
    infile2.close()
    return found

def find_districts( sdensity, inname ):
    """
    Reads the lines from the input file and from each line extracts the district
    name and density.  Finds and returns a string containing the names of all
    district with density below the value passed as a parameter. 
    Returns an empty string if no matching districts found. 

    Parameters:
    sdensity(float): density to search
    inname (string): name of file containing district/density data
    
    Returns:
    string: names of districts, empty string if none found

    """
    
    districts = ''
    infile = open( inname )
    for line in infile:
        d_pos = line.find(',')
        if float(line[d_pos+1:]) < sdensity:
            district = line[0:d_pos]
            districts += district + '\n'
    infile.close()
    return districts


