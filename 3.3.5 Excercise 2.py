# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:17:22 2020

@author: Tyler H
"""


lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

#lyrics = ["This was a triumph", "I'm making a note here: huge success", "It's hard to overstate my satisfaction"]
#lines_of_sanity = 8

#Imagine you have a song stuck in your head. Worse, you have
#only a few lines from a song stuck in your head. They just
#keep repeating over and over. The specific lines you have
#stuck in your head are stored in the variable lyrics.
#
#You can only stay sane so long while doing this.
#Specifically, you can only listen to lines_of_sanity lines
#before going crazy. Once you've reached lines_of_sanity,
#your brain will finish out the current list, then crumble.
#
#Write some code that will print the lyrics that run through
#your head. It should keep repeating each line one-by-one
#until you've reached lines_of_sanity lines. Then, it should
#keep going to finish out the current verse. After that, print
#"MAKE IT STOP" in all caps (without the quotes).
#
#HINT: Remember, we can iterate through items in a list using
#this syntax:
#
#  for item in list_of_items:
#
#HINT 2: You'll probably need a counter to count how many lines
#have been printed so far.

count = 0

if lines_of_sanity % len(lyrics) != 0:
    lines_of_sanity =  lines_of_sanity - (lines_of_sanity % len(lyrics)) + len(lyrics)
#    print(lines_of_sanity)
    
for word in range(0, lines_of_sanity):
#    print(count)
    if count == len(lyrics):
        count = 0
    print(lyrics[count])
    count += 1
#    print(word)

print("MAKE IT STOP")










