#!/usr/bin/env python
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import *


plt.xlabel('Current')
plt.ylabel('Voltage')

plt.axis([0,5,0,25])
plt.ion()
plt.show()
x=[1]
y=[1]
counter=1

vfile=open('cdata.txt','r')
cfile=open('vdata.txt','r')

while True:
    counter=counter+1
    cfile_data=cfile.readline()
    vfile_data=vfile.readline()
    print cfile_data,vfile_data
    x.append(Decimal(cfile_data))
    y.append(Decimal(vfile_data))
    #plt.plot(x,y)
    plt.scatter(x,y)
    #plt.relim()
    plt.autoscale(True)
    plt.draw()
    time.sleep(1)
    if counter==10:
        while True:
            pass
