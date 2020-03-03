# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:12:02 2017

@author: Tyler H
"""
from numpy import *
from matplotlib.pyplot import *
from scipy import signal
from control.matlab import *

num=[11.1, 11.1*18]
den=[1, 24, 90, 200]

sys = signal.TransferFunction(num, den, dt=1)

x, y =step(sys)
plot(x,y)


