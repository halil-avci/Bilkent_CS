# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:07:31 2019

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np

weight = np.array([2,3,4,5,10,16,22,26])
time = np.array([15,20,35,36,80,100,120,180] )

#plot the weight vs time first without fitting the curve
plt.plot(weight, time, 'bo') 

coef = np.polyfit(weight, time, 1)
y1= np.polyval(coef, weight) 
plt.plot(weight, y1, 'r-') 
plt.title('Burning Time of Candle')
plt.xlabel('Weight of Candle')
plt.ylabel('Burning Time')
plt.axis([0,30, 0,200])
plt.show()