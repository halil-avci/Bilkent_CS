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
plot([0],[0], 'bo')

Homer = UsualDrunk('Homer')
origin = Location(0, 0)
f = Field()

distances = []
for i in range(10):
    f.addDrunk(Homer, origin)
    distances.append(walk(f, Homer,100000))
    plot([f.getLoc(Homer).getX()],[f.getLoc(Homer).getY()], 'ro')
    print(distances[len(distances)-1])
    print(f.getLoc(Homer))

mean = sum(distances)/len(distances)
minDist = min(distances)
maxDist = max(distances)
print("Average Distance:"+str(mean))
print("Max Distance:"+str(maxDist))
print("Min Distance:"+str(minDist))


