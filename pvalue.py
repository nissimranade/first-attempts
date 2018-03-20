# -*- coding: utf-8 -*-
#p-value
"""
Created on Sun Mar 18 17:10:39 2018

@author: Nissim
"""

import matplotlib.pyplot as plt
import random


def f(): 
    return abs(random.normalvariate(.2, 7) ** (int(3 * random.random())))

L = []
c1 = 0
for i in range(10**6):
    L.append(i)
    L[i] = f()
    if L[i]>1000
        c1 = c1+1

plt.xlim([min(L)-5, max(L)+5])
plt.hist(L, bins=100, alpha=1)
plt.show()



K = []
c2 = 0
for j in range(10**6):
    K.append(j)
    K[j] = f()
    for i in range (19):
        y = f()
        if y > K[j]: 
            K[j] = y    
    c2 = c2 +1

plt.xlim([min(K)-5, max(L)+5])
plt.hist(K, bins=100, alpha=1)
plt.show()
