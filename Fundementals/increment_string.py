# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:24:50 2017

@author: georg

Your job is to write a function which increments a string, to create a 
new string. If the string already ends with a number, the number should be 
incremented by 1. If the string does not end with a number the number 1 
should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

"""

def increment_string(string):
    if string == "" or string[-1].isalpha():
        return string + "1"
    
    number = string
    word = ""
    for i in range(len(string) - 1, -1, -1):
        if not string[i].isnumeric():
            number = string[i + 1:]
            word = string[:i + 1]
            break
    
    print (number)
    incremented = (str(int(number)  + 1 ))
    
    if len(str(incremented)) >= len(str(number)):
        return word + incremented
    else:
        return word + "0" * (len(number) - len(str(incremented))) + incremented
    

    

print (increment_string("foobar1"))