# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import matplotlib.pyplot as plt

plt.clf()

# Pie chart,slices will be ordered, 
# plotted counter-clockwise:

pie_labels = 'Frogs', 'Hogs', 'Dogs', 'Cats'
sizes = [25, 35, 45, 10]

# only "explode" the 2nd slice(i.e. 'Hogs')
#explode = (0, 0.1, 0, 0)

plt.pie(sizes,labels = pie_labels, explode = (0,0,0.2,0), autopct='%.1f%%')
plt.title('Comparison of Animal Sizes')
#plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%')
