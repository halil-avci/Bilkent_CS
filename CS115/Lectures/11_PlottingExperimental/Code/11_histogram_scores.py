# ,-*- coding: utf-8 -*-
"""
@author: CS115
"""
import numpy as np
import matplotlib.pyplot as plt

score_arr = np.loadtxt('scores.csv',skiprows=1)

plt.figure(1) #opens a new active figure window
plt.clf() #clears the figure window

ax = plt.subplot(2,1,1)
res = plt.hist(score_arr,5) #plots scores with 5 bins/buckets
#ax.set_xticks(res[1])
plt.xticks(res[1])
plt.title('Bins set to 5')
plt.axis([2,19,2,12])

ax = plt.subplot(2,1,2)
plt.hist(score_arr, color = 'red') 
plt.title('Bins not specified (default:10)')





