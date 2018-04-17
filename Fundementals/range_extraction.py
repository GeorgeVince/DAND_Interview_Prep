# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:28:29 2018

@author: georg

A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the 
    end integer in the range by a dash, '-'. The range includes all integers in the 
    interval including both endpoints. It is not considered a range unless it spans 
    at least 3 numbers. For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order 
and returns a correctly formatted string in the range format. 
"""

import unittest

def solution(data_in):

    i = 0 
    to_return = ""
    while i < len(data_in):
        
        low = data_in[i]
        
        while i < len(data_in) - 1 and data_in[i] - data_in[i + 1] == -1:
            i += 1
            
        print ("called")   
        hi = data_in[i]
        
        if hi - low >= 2:
            to_return = to_return + str(low) + "-" + str(hi)
        elif hi - low == 1:
            to_return = to_return + str(low) + "," + str(hi)
        else:
            to_return = to_return + str(low)
        
        to_return = to_return + ","
        i += 1
    
    return to_return[:-1]


 
print(solution([1,2,3,4,5, 9,10,11,100]))
