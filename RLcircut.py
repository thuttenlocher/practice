# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 21:38:52 2016

@author: yub
"""

from pylab import *
from scipy import *

import control

p_list=[0.1,1,10,50]
t=arange(0,10,0.01)

for p in p_list:
    V_out=5.0*exp(-p*t)
    plot(t,V_out,label='p=%g' % p)
xlabel('t')
ylabel('$V_out$')
legend(loc=4)
savefig('RL_circuit.png', dpi=200)