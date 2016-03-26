# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:44:18 2016

@author: Lucky
"""

print '《99乘法表》'
for i in range(1,10) :
    for j in range(1,i+1):
        z = i * j
        print "%d * %d=%d" %(j,i,z),
    print
        
