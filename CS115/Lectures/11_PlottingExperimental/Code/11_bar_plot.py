# -*- coding: utf-8 -*-
"""
@author: CS115
"""
import matplotlib.pyplot as plt
import numpy as np


plt.clf()
n_groups = 5
index = np.arange(n_groups)

means_men = (20, 35, 30, 35, 27)
means_women = (25, 32, 34, 20, 25)

plt.bar(index,means_men, 0.4, align='edge')
plt.bar(index, means_women, -0.4, align = 'edge')
#plt.bar(index,means_men,  align = 'edge')
#plt.bar(index, means_women, -0.4, align= 'edge')


plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend(['Men', 'Women'])
