# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:27:34 2019

@author: b
"""

import numpy as np
import matplotlib.pyplot as plt

student = np.loadtxt('students.txt', skiprows=1)
half = student[student[:,0] == 2]

plt.figure(1)
plt.clf()


plt.subplot(2,4,1)
plt.title('Frequency of Math Gr. of Full Sc. Students')
plt.hist(half[:,3],4)

plt.subplot(2,4,4)
plt.title('Math vs Reading Gr. of Half Sc. Students')
plt.plot(half[:,1],':mo')
plt.plot(half[:,2], '-cx')
plt.ylabel('Grades')
plt.legend(['Math', 'Reading'])

plt.subplot(2,4,5)
plt.title('Scholarship Percentages')
t_data = [np.sum(student[:,0] == 1),np.sum(student[:,0] == 2), np.sum(student[:,0] == 3)]
labels = ('Full', 'Half', 'Non')
explode = (0, 0, 0.1)
plt.pie(t_data,labels=labels,autopct='%1.1f%%', explode = explode)

plt.subplot(2,4,8)
plt.bar('Half-sc.',np.mean(half[:,2]))
plt.bar('All',np.mean(student[:,2]))
plt.ylabel('Average of Grades')
plt.title('Reading Grades: Half Sc. vs All Students')













