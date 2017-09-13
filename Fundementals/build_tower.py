# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:47:31 2017

@author: georg

Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

    Python: return a list;
    JavaScript: returns an Array;
    C#: returns a string[];
    PHP: returns an array;
    C++: returns a vector<string>;
    Haskell: returns a [String];

Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]


"""


def tower_builder(n_floors):
    tower = []

    for i in range(0, n_floors):
        white_space = " " * int(( (2 * (n_floors -1) + 1) - (2 * i + 1) ) / 2)
        block = "*" * int(2 * i + 1)
        tower.append(white_space + block + white_space)
        print (white_space + block + white_space)
    return tower


print (tower_builder(6))

