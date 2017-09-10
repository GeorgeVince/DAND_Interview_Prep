# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:26:37 2017

@author: georg

In a factory a printer prints labels for boxes. For one kind of boxes the 
printer has to use colors which, for the sake of simplicity, are named with 
letters from a to m.

The colors used by the printer are recorded in a control string. For example a 
"good" control string would be aaabbbbhaijjjm meaning that the printer used three 
times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a 
"bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

You have to write a function printer_error which given a string will output 
the error rate of the printer as a string representing a rational whose numerator 
is the number of errors and the denominator the length of the control string. 
Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters 
from ato z.

#Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"

"""
PERMITTED_COLOURS = "abcdefghijklm"

def printer_error(s):
    # your code
    to_return = 0
    for char in s:
        if char not in PERMITTED_COLOURS:
            to_return = to_return + 1
    
    return "{}/{}".format(to_return, len(s))

s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print (printer_error(s))