# -*- coding: utf-8 -*-
#p-value
"""
Created on Sun Mar 18 17:10:39 2018

@author: Nissim
"""

import random

def f(): 
    return abs(random.normalvariate(.2, 7) ** (int(3 * random.random())))

print "Experiment 1"

for i in range(1,20):
    print f()

print "Experiment 2" 

for j in range(1, 20):
    x = f()
    for i in range (1,19):
        y = f()
        if y > x: 
            x = y    
            print y
