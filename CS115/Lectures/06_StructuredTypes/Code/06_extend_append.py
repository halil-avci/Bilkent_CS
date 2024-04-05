# -*- coding: utf-8 -*-
"""
@author: CS115
"""
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =',L3)
L1.extend(L2)
print('L1 =',L1)
L1.append(L2)
print('L1 =',L1)