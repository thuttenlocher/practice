
from pylab import *
from scipy import *
from scipy import optimize
import control
#load data 
data1=loadtxt('trial 1.txt',skiprows=1)
data2=loadtxt('trial 2.txt',skiprows=1)
data3=loadtxt('trial 3.txt',skiprows=1)
data4=loadtxt('trial 4.txt',skiprows=1)
data5=loadtxt('trial 5.txt',skiprows=1)  #load the file called data.txt

x1=data1[:,0]    #assign first colume of data.txt to variable x
y1=data1[:,2]

x2=data2[:,0]    #assign first colume of data.txt to variable x
y2=data2[:,2]

x3=data3[:,0]    #assign first colume of data.txt to variable x
y3=data3[:,2]           

x4=data4[:,0]    #assign first colume of data.txt to variable x
y4=data4[:,2]          

x5=data5[:,0]    #assign first colume of data.txt to variable x
y5=data5[:,2]    #assign second colume of data.txt to variable y

#print (x)
v5=data5[:,1]
figure(1)      #create a figure
clf()          #clear the figure
plot(x5,y5,'ro',label='$T_{exp}$')   #plot first colume data vs the second colume data

# a cost function that is compatible with fmin
def fitmodel(c):                    # define a fitmodel function
        G=control.tf(c[0],[1,c[1]])
        out=control.forced_response(G,x5,v5)
        yy=out[1]+25.34
        #y1=(c[0])/(x+c[1])     # this is the model I use to curve fit the data c[0] and c[1] are my guesses
        return yy
def mycost(c):                      # define a mycost function
        fit_result=fitmodel(c)      # the output for the fitmodel
        e=(yy-fit_result)**2         # e is total difference between the data and my model
        return sum(e)

ig=[.3359,.0193]                            # assign a inital guess to the model's unknown coefficients

y_ig= fitmodel(ig)               # run fitmodel function based on the initial guess for the unknow coefficients

plot(x5,y_ig,'-g',label='$T_{ig}$')   # plot the output of the guess model


run_fit=1                         # if run_fit=1 will run optimize.fmin if run_fit=0 will not run optimize.fmin
if run_fit:
        op_c1 = optimize.fmin(mycost,ig)
        y_fit1 = fitmodel(op_c1)
                
        plot(x5,y_fit1,label='$T_{fit}$')
print(op_c1)

legend(loc=4)                          #legend location 
xlabel('Temperature [\u2103]')                            #label your x-axis
ylabel('Time [s]')                         #label your y-axis
title('Step Response')
# plots the final result for the curve fit 
show()

#print (x)
figure(2)      #create a figure
clf()          #clear the figure
                                   #plot first colume data vs the second colume data
plot(x1,y1,'r.',label='$T_{1}$')
plot(x2,y2,'b+',label='$T_{2}$')
plot(x3,y3,'g3',label='$T_{3}$')
plot(x4,y4,'md',label='$T_{4}$')
plot(x5,y5,'cx',label='$T_{5}$') 

legend(loc=4)                          #legend location 
xlabel('Temperature [\u2103]')                            #label your x-axis
ylabel('Time [s]')                         #label your y-axis
title('Test Results Data')
# plots the final result for the curve fit 
show()


figure(3)      #create a figure
clf()          #clear the figure

plot(x1,y1,'r.',label='$T_{1}$')
plot(x2,y2,'b+',label='$T_{2}$')
plot(x3,y3,'g3',label='$T_{3}$')
plot(x4,y4,'md',label='$T_{4}$')
plot(x5,y5,'cx',label='$T_{5}$') 
plot(x5,y_ig,'-k',label='$T_{ig}$')
plot(x5,y_fit1,label='$T_{fit}$')

legend(loc=4)                          #legend location 
xlabel('Temperature [\u2103]')                            #label your x-axis
ylabel('Time [s]')                         #label your y-axis
title('Test Results Overlayed with Test Response ')
# plots the final result for the curve fit 
show()   
   