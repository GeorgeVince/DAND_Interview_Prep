# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:20:37 2017

@author: georg

You are given an array strarr of strings and an integer k. Your task is to 
return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", 
"theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""

def longest_consec(strarr, k):
    longest = ""
    if k > 0:
        for indx in range(0, len(strarr) - (k - 1)):
            consec_string = ("".join(strarr[indx:indx + (k) ]))
            if len(consec_string) > len(longest):
                longest = consec_string
            
    return longest
        
        
#print (longest_consec(['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb', 'oocccffuucccjjjkkkjyyyeehh'], -1) )
print (longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 1))