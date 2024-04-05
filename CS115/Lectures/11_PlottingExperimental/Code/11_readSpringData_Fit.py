# -*- coding: utf-8 -*-
"""
@author: CS115
"""
from matplotlib.pyplot import *
from numpy import *

def getData(filename):
    dataFile = open(filename, 'r')
    distances = []
    masses = []
    dataFile.readline()
    for line in dataFile:
        d,m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return(masses, distances)

def fitData(inputfile):
    masses, distances = getData(inputfile)
    forces = []
    for m in masses:
        forces.append(m * 9.81) #9.81 represents gravitational force
    plot(forces, distances, 'ro',label = 'Measured Displacements')
    title('Measured Displacement of Spring')
    xlabel('|Force|(newtons)')
    ylabel('Distance(meters)')
    
     #find linear fit using loop
#    a,b = polyfit(forces, distances, 1)
#    predictedDistances = []
#    for f in forces:
#         predictedDistances.append(a*f+b)
#    plot(forces, predictedDistances, label = 'Displacements predicted by '\
#                                                   'linear fit')
    #find linear fit using polyval
    fit = polyfit(forces, distances, 1)
    predictedDistances = polyval(fit, forces)
    plot(forces, predictedDistances, label = 'Displacements predicted by '\
                                                   'linear fit')
    legend(loc = 'best')    

clf()
fitData('11_springData.txt')
           