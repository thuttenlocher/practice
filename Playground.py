# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:12:10 2020

@author: Tyler H
"""





entered = "abc123"
password = "abc123"
tries = 3

#Above we've created three variables representing an attempt
#to enter a password. Add some code below that will print the
#result of this check:
#
# - "Login successful." if entered is the same as password
#   and tries is less than or equal to 3.
# - "Incorrect password." if entered is not the same as 
#   password, but tries is less than or equal to 3.
# - "Tries exceeded." if tries is greater than 3.
#
#You don't need to worry about incrementing tries if the
#password is incorrect.


if entered == password and tries <=3:
    print("Login successful.")
else:
    if entered != password and tries <=3:
        print("Incorrect password.")
    else:
        print("Tries exceeded.")







