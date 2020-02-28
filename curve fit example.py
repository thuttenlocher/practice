
from pylab import *
from scipy import *
from scipy import optimize
import control
#load data 
data=loadtxt('trial 5.txt',skiprows=1)  #load the file called data.txt

x=data[:,0]    #assign first colume of data.txt to variable x
y=data[:,2]    #assign second colume of data.txt to variable y
#print (x)
v=data[:,1]
figure(1)      #create a figure
clf()          #clear the figure
plot(x,y,'ro',label='$T_{exp}$')   #plot first colume data vs the second colume data

# a cost function that is compatible with fmin
def fitmodel(c):                    # define a fitmodel function
        G=control.tf(c[0],[1,c[1]])
        out=control.forced_response(G,x,v)
        y1=out[1]+25.34
        #y1=(c[0])/(x+c[1])     # this is the model I use to curve fit the data c[0] and c[1] are my guesses
        return y1
def mycost(c):                      # define a mycost function
        fit_result=fitmodel(c)      # the output for the fitmodel
        e=(y-fit_result)**2         # e is total difference between the data and my model
        return sum(e)

ig=[.3359,.0193]                            # assign a inital guess to the model's unknown coefficients

y_ig= fitmodel(ig)               # run fitmodel function based on the initial guess for the unknow coefficients

plot(x,y_ig,'-g',label='$T_{ig}$')   # plot the output of the guess model


run_fit=1                         # if run_fit=1 will run optimize.fmin if run_fit=0 will not run optimize.fmin
if run_fit:
        op_c1 = optimize.fmin(mycost,ig)
        y_fit1 = fitmodel(op_c1)
                
        plot(x,y_fit1,label='$T_{fit}$')
print(op_c1)

legend(loc=4)                          #legend location 
xlabel('Temperature [\u2103]')                            #label your x-axis
ylabel('Time [s]')                         #label your y-axis
title('Step Response')
# plots the final result for the curve fit 
show()
