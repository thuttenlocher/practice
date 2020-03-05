# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:07:58 2016

@author: yub
"""
from pylab import *
from scipy import *
from scipy import optimize

import control

vect=[2.0,2.5,3.0,3.5294,3.92157]
N=len(vect)
#a1=6.5*A
b1=34.5
ambientT=21.27

data = loadtxt('dc_102.txt', skiprows=1)
data1 = loadtxt('dc_128.txt', skiprows=1)
data2 = loadtxt('dc_153.txt', skiprows=1)
data3 = loadtxt('dc_180.txt', skiprows=1)
data4 = loadtxt('dc_200.txt', skiprows=1)

figure(1)
clf()

DATA=[data,data1,data2,data3,data4]

for i in range(N):
	mylabel='$exp = %0.3g$' % vect[i]
	mylabe2='$theo = %0.3g$' % vect[i]
	Data=DATA[i]
	plot(Data[:,0],Data[:,2],label=mylabel)
	A=vect[i]
	a1=6.5*A
	G = control.TransferFunction(a1,[b1,1])
	t1, y1 = control.step_response(G,data[:,0])
	y1=y1+ambientT
	plot(t1,y1,'o',label=mylabe2)
 

xlabel('Time (sec.)')
ylabel('$y(t)$')
title('Simulation Overlay Experimental')
legend(loc=4)
savefig('1nd order.png',dpi=200)	

show()
