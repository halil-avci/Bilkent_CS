# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:07:31 2019

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np

initial = np.arange(30,75,5)
bounce = np.array([22,26,29,34,38,40,45,50,52] )

#plot the initialerature vs bounceity first without fitting the curve
plt.plot(initial, bounce, 'bo') 

coef = np.polyfit(initial, bounce, 1)
y1= np.polyval(coef, initial) 

plt.plot(initial, y1, 'r-') 
plt.title('Initial Height vs. Bounce Height')
plt.xlabel('Initial Height')
plt.ylabel('Bounce Height')
plt.show()