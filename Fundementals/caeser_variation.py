# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:11:52 2017

@author: georg

The action of a Caesar cipher is to replace each plaintext letter with a different 
one a fixed number of places up or down the alphabet.

This program performs a variation of the Caesar shift. The shift increases by 
1 for each character (on each iteration).

If the shift is initially 1, the first character of the message to be encoded 
will be shifted by 1, the second character will be shifted by 2, etc...
Coding: Parameters and return of function "movingShift"

param s: a string to be coded

param shift: an integer giving the initial shift

The function "movingShift" first codes the entire string and then returns an 
array of strings containing the coded string in 5 parts (five parts because, 
to avoid more risks, the coded message will be given to five runners, one piece 
for each runner).

If possible the message will be evenly split between the five runners; if not 
possible, parts 1, 2, 3, 4 will be longer and part 5 shorter. The fifth part can 
have length equal to the other ones or shorter. If there are many options of how 
to split, choose the option where the fifth part has the longest length, provided 
that the previous conditions are fulfilled. If the last part is the empty string 
this empty string must be shown in the resulting array.

For example, if the coded message has a length of 17 the five parts will have 
lengths of 4, 4, 4, 4, 1. The parts 1, 2, 3, 4 are evenly split and the last 
part of length 1 is shorter. If the length is 16 the parts will be of lengths 
4, 4, 4, 4, 0. Parts 1, 2, 3, 4 are evenly split and the fifth runner will stay 
at home since his part is the empty string.

You will also implement a "demovingShift" function with two parameters
Decoding: parameters and return of function "demovingShift"

1) an array of strings: s (possibly resulting from "movingShift", with 5 strings)

2) an int shift

"demovingShift" returns a string.
Example:

u = "I should have known that you would have a perfect answer for me!!!"

movingShift(u, 1) returns :

v = ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

(quotes added in order to see the strings and the spaces, 
your program won't write these quotes, see Example Test Cases)

and demovingShift(v, 1) returns u.

"""

def split(a, n):
    k, m = divmod(len(a), n)
    first_split = list((a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)))
    l = len(first_split[0])
    
    #Check if list 1 - 4 are equal
    if (all(len(item) == len(first_split[0]) for item in first_split[:-1])):
        return first_split
   #Else split then and add remainder
    else:
        l = len(first_split[0])
        for i in range(0, 4):
           first_split[i] = a[i * l : (i + 1) * l ]
        
        if 4 * l < len(a):
            first_split[4] = a[4 * l:]
        else:
            first_split[4] = ""
    
    return first_split

def translate_message(mode, s, shift):
    to_return = ""
    key = shift % 26

    for char in s:
        if char.isupper() or char.islower():
            if mode[0] == "e":  
                new_char = ord(char) + key
            else:
                new_char = ord(char) - key
            
            if char.isupper():
                upper_limit = "Z"
                lower_limit = "A"
            else:
                upper_limit = "z"
                lower_limit = "a"
            if new_char > ord(upper_limit):
                new_char -= 26
            elif new_char < ord(lower_limit):
                new_char += 26
            
            to_return += chr(new_char)
        else:
            to_return += char
        
        key += 1
        key = key % 26
    
    return list(split(to_return, 5))


def moving_shift(s, shift):
    return translate_message("e", s, shift)
      

def demoving_shift(s, shift):
    s = "".join(s)
    return "".join(translate_message("d", s, shift))



