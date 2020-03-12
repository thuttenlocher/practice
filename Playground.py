# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:12:10 2020

@author: Tyler H
"""




mystery_int = 5

#In math, factorial is a mathematical operation where an
#integer is multipled by every number between itself and 1.
#For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
#Factorial is represented by an exclamation point: 5!
#
#Use a for loop to calculate the factorial of the number
#given by mystery_int above. Then, print the result.
#
#Hint: Running a loop from 1 to mystery_int will give you
#all the integers you need to multiply together. You'll need
#to track the total product using a variable declared before
#starting the loop, though!
num = 1

for i in range(1, mystery_int + 1):
    num = i * num
print(num)





