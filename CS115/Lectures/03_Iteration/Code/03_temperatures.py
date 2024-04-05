"""
@author: cs115
"""
import sys

maxTemp = sys.float_info.min
maxMonth = 0

for mon in range(1,12):
    temp = float(input("Enter temperature: "))
    if temp > maxTemp:
        maxTemp = temp
        maxMonth = mon
        
print("The maximum temperature of "+str(maxTemp) +
      " occured in month "+str(maxMonth))