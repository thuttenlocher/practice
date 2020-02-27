
from pylab import *
from scipy import *
#from scipy import optimize
#load data 
data=loadtxt('data.txt',skiprows=1)  #load the file called data.txt

x=data[:,0]    #assign first colume of data.txt to variable x
y=data[:,1]    #assign second colume of data.txt to variable y
#print (x)
figure(1)      #create a figure
clf()          #clear the figure
plot(x,y,'ro',label='$y_{exp}$')   #plot first colume data vs the second colume data

# a cost function that is compatible with fmin
def fitmodel(c):                    # define a fitmodel function
        y1=(x+c[0])**2+c[1]         # this is the model I use to curve fit the data c[0] and c[1] are my guesses
        return y1
def mycost(c):                      # define a mycost function
        fit_result=fitmodel(c)      # the output for the fitmodel
        e=(y-fit_result)**2         # e is total difference between the data and my model
        return sum(e)

ig=[-2.7,0.6]                       # assign a inital guess to the model's unknown coefficients

y_ig= fitmodel(ig)                  # run fitmodel function based on the initial guess for the unknow coefficients

plot(x,y_ig,'-g',label='$y_{ig}$')   # plot the output of the guess model


run_fit=1                             # if run_fit=1 will run optimize.fmin if run_fit=0 will not run optimize.fmin
if run_fit:
        op_c1 = optimize.fmin(mycost,ig)
        y_fit1 = fitmodel(op_c1)
                
        plot(x,y_fit1,label='$y_{fit}$')
print(op_c1)

legend(loc=4)                          #legend location 
xlabel('x')                            #label your x-axis
ylabel('y(x)')                         #label your y-axis
# plots the final result for the curve fit 
show()
