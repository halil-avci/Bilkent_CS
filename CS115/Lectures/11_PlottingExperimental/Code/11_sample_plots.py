# -*- coding: utf-8 -*-
"""
@author: CS115
"""

from matplotlib.pyplot import *
clf()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Cats'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')


pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%')
