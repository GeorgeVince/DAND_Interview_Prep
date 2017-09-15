# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:51:20 2017

@author: georg

The word i18n is a common abbreviation of internationalization the developer 
community use instead of typing the whole word and trying to spell it correctly. 
Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) 
within that string of length 4 or greater into an abbreviation following the 
same rules.

Notes:

    A "word" is a sequence of alphabetical characters. By this definition, 
    any other character like a space or hyphen (eg. "elephant-ride") will 
    split up a series of letters into two words (eg. "elephant" and "ride").
    The abbreviated version of the word should have the first letter, then 
    the number of removed characters, then the last letter 
    (eg. "elephant ride" => "e6t r2e").

"""
def shorten_word(word):
    to_return = ""
    gap = str(len(word)-2)
    
    if len(word) > 3:
        to_return += str(word[0]) + gap + word[len(word) - 1]
    else: 
        to_return = word
    
    return to_return
    

def abbreviate(s):
    curr_word = ""
    to_return = ""
    for char in s:
        if char.isalpha():
            curr_word += char
        else:
            to_return += shorten_word(curr_word)
            to_return += char
            curr_word = ""
    
    if to_return == "":
        to_return += shorten_word(curr_word)
    return to_return
            
            
print (abbreviate("sat-sat. the; a'cat, balloon; sits; sat; is:"))