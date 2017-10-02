# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 18:33:13 2017

@author: georg

Given a string and an array of integers representing indices, capitalize all 
letters at the given indices.

For example:

    capitalize("abcdef",[1,2,5]) = "aBCdeF"
    capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.

The input will be a lowercase string with no spaces and an array of digits.

Good luck!


"""

'Credit: 
'https://stackoverflow.com/questions/8217650/change-some-lowercase-letters-to-uppercase-in-string

def capitalize(s,ind):
    return ("".join(c.upper() if i in ind else c for i, c in enumerate(s)))

print (capitalize("abcdef",[1,2,5,55]))