# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import pylab

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

def plotData(inputfile):
    masses, distances = getData(inputfile)
    forces = []
    for m in masses:
        forces.append(m * 9.81) #9.81 represents gravitational force
    pylab.plot(forces, distances, 'ro')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force(newtons)')
    pylab.ylabel('Distance(meters)')
    
plotData('11_springData.txt')
           