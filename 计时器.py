# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:16:55 2016

@author: Lucky
"""

#计时器
import time
import sys
def timer(num):
    for i in range(0,61) :
        sys.stdout.write('\r%d'%(i))
        sys.stdout.flush()
        time.sleep(1)
if __name__ =='__main__' :
    timer(60)

sys.stdout.write('#'*20)
sys.stdout.flush()   
while True :
    for i in range(0,22) :
        sys.stdout.write('\r%sa'%('#'*i))
        sys.stdout.flush()
        time.sleep(0.5)