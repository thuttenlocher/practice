import control
from pylab import *
from scipy import *
from numpy import *

G2=control.ss("0 1 0; 0 0 1; -8 -6 -4", "0; 0; 20", "1 0 0", "0")
G3=control.ss("0 1 0; 0 0 1; -8 -6 -4", "0; 0; 20", "0 1 0", "0")
t3,y3=control.step_response(G2)
t4,y4=control.step_response(G3)

figure(2)
clf()
plot(t3,y3, 'ro',label='y')
plot(t4,y4, 'bx', label='$y_{dot}$')
xlabel('Time')
ylabel('$y(t)$')
legend(loc=4)



