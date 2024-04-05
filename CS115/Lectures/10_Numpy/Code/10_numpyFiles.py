# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import numpy as np
#load data containing population and area
data = np.loadtxt("10_world_pop_area.txt", skiprows=1)
print(data)

#load country names from text file
cData = np.loadtxt("10_countries.txt", dtype='str')

#find the expected population after 1 year (assume 10% increase)
data[:, 0] = data[:, 0] * 1.1

#calculate density
density = data[:,0] / data[:,1]

#store countries and densities in new array
file_data = np.array([cData,density])

#write the countries and names and density to file
np.savetxt("densities.txt",file_data.T, fmt='%s')

#find the country with the greatest density
maxIndex = density.argmax()
print('Country with maximum density: ',cData[maxIndex])
print('Density: ',density.max(),'km2')

