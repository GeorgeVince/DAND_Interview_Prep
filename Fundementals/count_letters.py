# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:36:09 2017

@author: georg

The main idea is to count all the occuring characters(UTF-8) in string. 
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
"""
from collections import defaultdict

def count(string):
    # The function code should be here
    to_return = defaultdict(int)
    for c in string:
        to_return[c] += 1
    
    return to_return


print (count("abcabc"))