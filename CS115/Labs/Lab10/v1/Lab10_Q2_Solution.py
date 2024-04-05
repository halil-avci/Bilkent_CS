# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:27:34 2019

@author: b
"""

import numpy as np
import matplotlib.pyplot as plt

student = np.loadtxt('students.txt', skiprows=1)
full = student[student[:,0] == 1]

plt.figure(1)
plt.clf()


plt.subplot(2,4,1)
plt.title('Frequency of Math Gr. of Full Sc. Students')
plt.hist(full[:,1],3)

plt.subplot(2,4,4)
plt.title('Reading vs Writing Gr. of Full Sc. Students')
plt.plot(full[:,2],'-.rd')
plt.plot(full[:,3], ':ks')
plt.ylabel('Grades')
plt.legend(['Reading', 'Writing'])

plt.subplot(2,4,5)
plt.title('Scholarship Percentages')
t_data = [np.sum(student[:,0] == 1),np.sum(student[:,0] == 2), np.sum(student[:,0] == 3)]
labels = ('Full', 'Half', 'Non')
explode = (0, 0, 0.1)
plt.pie(t_data,labels=labels,autopct='%1.1f%%', explode = explode)

plt.subplot(2,4,8)
plt.bar('Full-sc.',np.mean(full[:,1]))
plt.bar('All',np.mean(student[:,1]))
plt.ylabel('Average of Grades')
plt.title('Comparison of Math Grades: Full Sc. vs All Students')













