# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:01:30 2020

@author: A6DB5ZZ
"""

#Write a function called total_volume. total_volume should
#have four parameters, all integers. The first three
#parameters should represent the length, width, and height
#of a box respectively. The fourth should represent the
#number of boxes.
#
#The function should return an integer representing the
#total volume represented by the given boxes. For example,
#if the length is 10, the width is 2, the height is 2, and
#there are 4 boxes, then the total volume would be 160:
#((10 * 2 * 2) * 4) = 160.


test_box_count = 4
def total_volume(test_length, test_width, test_height, test_box_count):
    return test_length * test_width * test_height * test_box_count

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".
test_length = 10
test_width = 2
test_height = 2
test_box_count = 4
result = total_volume(test_length, test_width, test_height, test_box_count)
print(result)


