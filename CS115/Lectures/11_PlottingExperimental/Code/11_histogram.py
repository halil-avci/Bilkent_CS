# -*- coding: utf-8 -*-
"""
@author: CS115
"""
from matplotlib.pyplot import *
import random

def random_ints(num, lower, upper):
    ints = []
    for i in range(num):
        ints.append(random.randrange(lower,upper+1))
    return ints
clf()
data = random_ints(100, 1, 10)
n = hist(data,5)
