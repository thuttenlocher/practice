# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:22:23 2017

@author: Tyler H
"""

import control
data=loadtxt('trial 1.txt',skiprows=1)

T=1
s=.7

G=control.tf((1/T)/(s+(1/T)))

y,t=control.step_response(G,Time,Voltage,hmax=dt)


plot(y,t)
xlabel("Time")
ylabel("Displacement")
title("Step Response")