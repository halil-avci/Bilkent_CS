# -*- coding: utf-8 -*-
"""
@author: CS115
"""

from matplotlib.pyplot import *
from numpy import *
 

max_temp = random.randint(1,46,12)
min_temp =  random.randint(-20,20,12)
months = array(arange(1,13))

print(max_temp)
print(min_temp)

diff_temp = abs(max_temp - min_temp)
avg = mean(diff_temp)


print('Monthly differences: ', diff_temp)
print('Average difference: ',avg)
print('Months with difference above average:')

res = where(diff_temp > avg)
for r in res:
    print(r+1, end =' ')


clf()
subplot(1,2,1)
plot(months, max_temp)
plot(months, min_temp)

xlabel('Month')
ylabel('Temperature')
title('Comparison of Monthly Temperatures')
legend(['max temps', 'min temps'])
axis([1, 12, min(min_temp), max(max_temp)])

subplot(1,2,2)
plot(months, diff_temp)
xlabel('Month')
ylabel('Temperature Difference')
title('Monthly Differences')
axis([1, 12, min(diff_temp), max(diff_temp)])
