# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:12:10 2020

@author: Tyler H
"""

item = "quesadilla"
meat = "pork"
queso = True
guacamole = True
double_meat = False
#-----------------------------------------------------------
#Let's further expand our previous program to cover a broader
#menu variety. Instead of just burritoes, now the program
#should cover three menu items: quesadillas, burritoes, and
#nachos. Instead of separate booleans for steak and pork,
#we instead have a string that could be "steak", "pork",
#"chicken", "tofu", and "beef". We still have booleans for
#queso and guacamole, but we also have a boolean for double
#meat.
#
#Your code should calculate the price as follows:
#
# - The base price for a quesadilla is 4.00, for nachos is
#   4.50, and for burritoes is 5.00.
# - If meat is steak or pork, add 0.50. Any other meat adds
#   no money to the price.
# - guacamole always adds 1.00 to the price.
# - queso adds 1.00 to the price UNLESS the item is nachos,
#   in which case it adds nothing.
# - double_meat adds 1.50 if the meat is steak or pork, or
#   1.00 otherwise.

base_price = 4.5
if item == "quesadilla":
    base_price = 4.0
    print("ordered quesadilla")
elif item == "burrito":
    base_price = 5.0
    print("ordered burrito")
else:
    base_price += 0.0
    print("ordered nachos")

    
if meat == "pork":
    base_price += 0.50
    print("ordered pork")
elif meat == "steak":
    base_price += 0.50
    print("ordered steak")
else:
    base_price += 0.00
    print("didn't order steak or pork")

    
if meat == ("steak" or "pork") and double_meat:
    base_price += 1.50
    print("ordered steak or pork and double_meat")
elif double_meat:
    base_price += 1.0
    print("ordered double meat not of steak or pork")


if guacamole:
    base_price += 1.0
    print("ordered guacamole")

if queso and item != "nachos":
    base_price += 1.0
    print("ordered nachos")

    
    
print(base_price)




