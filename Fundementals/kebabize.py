# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:59:11 2017

@author: georg

Modify the kebabize function so that it converts a camel case string 
into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

Notes:

    the returned string should only contain lowercase letters


"""

def kebabize(string):
    to_return = ""
    for char in string:
        if char.isalpha() and char.islower():
            to_return += char
        elif char.isalpha() and char.isupper():
            to_return += "-" + char.lower() 
    
    if to_return:
        if to_return[0] == "-":
            return to_return[1:]
        else:
            return to_return    
    else: 
        return to_return

print (kebabize('32'))