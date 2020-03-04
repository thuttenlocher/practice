from pylab import *
from scipy import *

figure(1)                   # creat a figure
clf()                       # clear the figure

x = arange(0,2,0.01)       # creat a vector x from 0 to 2 with an interval of 0.01
y = exp(x)                 # calculate y= e(x)
plot(x,y,label='nonlinear model $y=e^x$' )                  # plot the nonlinear model
y_lin = e*x               # write the linear model
plot(x,y_lin,label='linearized model $y=ex$')              # plot the linear model

xlim([0.5,1.5])        # scale your x-axis
ylim([1,4])            # scale your y-axis

xlabel('$x$')          # label your x-axis
ylabel('$y$')          # label your x-axis

legend(loc=4)          # put a legend at location 4
savefig('linearization.png',dpi=200)   #save the plot

show()
