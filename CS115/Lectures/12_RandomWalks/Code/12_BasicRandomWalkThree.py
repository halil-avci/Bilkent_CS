# -*- coding: utf-8 -*-
"""
@author: CS115
"""
from matplotlib.pyplot import *
from Field import *
from Drunk import *
from Location import *

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the 
       walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

#random.seed(0)
clf()

f = Field()
for i in range(1,6):
    origin = Location(0, 0)
    f.addDrunk(UsualDrunk( 'Homer'+str(i)), origin)
drunks = f.getDrunks()
print(drunks)

print()
distances = []
drunks = f.getDrunks()
colors = ['ro', 'mo', 'bo', 'go', 'ko']
cPos = 0

for d in drunks:
    for i in range(10):
        f.addDrunk(d, origin)
        distances.append(walk(f, d,100000))
#        print(distances[len(distances)-1])
#        print(f.getLoc(d))
        plot([f.getLoc(d).getX()],[f.getLoc(d).getY()], colors[cPos])
    cPos += 1

mean = sum(distances)/len(distances)
minDist = min(distances)
maxDist = max(distances)
print("Average Distance:"+str(mean))
print("Max Distance:"+str(maxDist))
print("Min Distance:"+str(minDist))

#plot([0],[0], 'bo')
