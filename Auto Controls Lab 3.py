from pylab import *
from scipy import *
from scipy import optimize
import control

#load data 
data1=loadtxt('trial 1.txt',skiprows=1)  #load the file called trial 1.txt 
data2=loadtxt('trial 2.txt',skiprows=1)  #load the file called trial 2.txt
data3=loadtxt('trial 3.txt',skiprows=1)  #load the file called trial 3.txt
data4=loadtxt('trial 4.txt',skiprows=1)  #load the file called trial 4.txt
data5=loadtxt('trial 5.txt',skiprows=1)  #load the file called trial 5.txt

x1=data1[:,0]    #assign first column of trial 1.txt to variable x1
y1=data1[:,2]    #assign third column of trial 1.txt to variable y1

x2=data2[:,0]    #assign first column of trial 2.txt to variable x2
y2=data2[:,2]    #assign third column of trial 2.txt to variable y2

x3=data3[:,0]    #assign first column of trial 3.txt to variable x3
y3=data3[:,2]    #assign third column of trial 3.txt to variable y3         

x4=data4[:,0]    #assign first column of trial 4.txt to variable x4
y4=data4[:,2]    #assign third column of trial 4.txt to variable y4        

x5=data5[:,0]    #assign first column of trial 5.txt to variable x5
y5=data5[:,2]    #assign third column of trial 5.txt to variable y5

v1=data1[:,1]    #assign second column of trial 5.txt to variable v1
v2=data2[:,1]    #assign second column of trial 5.txt to variable v2
v3=data3[:,1]    #assign second column of trial 5.txt to variable v3       
v4=data4[:,1]    #assign second column of trial 5.txt to variable v4
v5=data5[:,1]    #assign second column of trial 5.txt to variable v5

figure(1)      #create a figure 1
clf()          #clear the figure
plot(x5,y5,'ro',label='$T_{exp}$')   #plot first column data vs the second column data

# a cost function that is compatible with fmin
def fitmodel(c):                    # define a fitmodel function
        G=control.tf(c[0],[1,c[1]])     # create a transfer function
        out=control.forced_response(G,x5,v5)    # simulate the output of the transfer function
        y5=out[1]+25.34                 
        return y5
def mycost(c):                      # define a mycost function
        fit_result=fitmodel(c)      # the output for the fitmodel
        e=(y5-fit_result)**2         # e is total difference between the data and my model
        return sum(e)

ig=[.3359,.0193]                 # assign a inital guess to the model's unknown coefficients

y_ig= fitmodel(ig)               # run fitmodel function based on the initial guess for the unknow coefficients

plot(x5,y_ig,'-g',label='$T_{ig}$')   # plot the output of the guess model

# generate a fit model
run_fit=1                         # if run_fit=1 will run optimize.fmin if run_fit=0 will not run optimize.fmin
if run_fit:
        op_c1 = optimize.fmin(mycost,ig)    # minimize function mycost
        y_fit1 = fitmodel(op_c1)
        plot(x5,y_fit1,label='$T_{fit}$')
print(op_c1)

legend(loc=4)                          #legend location 
xlabel('Time [s]')                            #label your x-axis
ylabel('Temperature [\u2103]')                         #label your y-axis
title('Step Response')              #label graph
# plots the final result for the curve fit 
show()

# calculate error
error_old=mycost(ig)    # calculate the error between the guessed model and experimental data
error_new=mycost(op_c1) # calculate the error between the optimized model and experimental data

# create a plot contianing the 5 data sets with transfer functions
vect=[2.25,1.96,1.67,1.37,1.08]     # create matrix containing voltages
N=len(vect)                         # store length of vect as N
#a1=6.5*A
b1=34.5
ambientT=25.34

figure(2)   # create a figure 2
clf()       # clear figure

DATA=[data1,data2,data3,data4,data5]    # create matrix containg data from 5 trials


for j in range(N):
    mylabel='$exp_%d = %0.3g$' % (j+1,vect[j])          # label for experimental data points
    mylabe2='$theo_%d = %0.3g$' % (j+1,vect[j])         # label for theoretical data points
    Data=DATA[j]                               
    plot(Data[:,0],Data[:,2],label=mylabel)    # plot data
    A=vect[j]
    a1=6.5*A
    G = control.TransferFunction(a1,[b1,1])    # create a transfer function
    t1, y1 = control.step_response(G,Data[:,0])    # create a step resonse
    y1=y1+ambientT                             # add ambient temperature to y value
    plot(t1,y1,'o',label=mylabe2)              # plot data

# label graph
xlabel('Time [s]')                              # label x-axis
ylabel('Temperature [\u2103]')                  # label y-axis
title('Simulation Overlay Experimental')        # label graph
legend(loc=4)                                   # create a legent
savefig('Simulation Overlay Experimental.png',dpi=200)	 # save figure

show()                
                          