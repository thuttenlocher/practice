
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
v=data5[:,1]
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
title('Test Results')
# plots the final result for the curve fit 
show()


figure(3)      #create a figure
clf()          #clear the figure

plot(x1,y1,'r.',label='$T_{1}$')
plot(x2,y2,'b+',label='$T_{2}$')
plot(x3,y3,'g3',label='$T_{3}$')
plot(x4,y4,'md',label='$T_{4}$')
plot(x5,y5,'cx',label='$T_{5}$') 

legend(loc=4)                          #legend location 
xlabel('Temperature [\u2103]')                            #label your x-axis
ylabel('Time [s]')                         #label your y-axis
title('Test Results and ')
# plots the final result for the curve fit 
show()   
   
   