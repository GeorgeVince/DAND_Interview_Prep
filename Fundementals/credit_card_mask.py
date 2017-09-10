# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:58:47 2017

@author: georg

Usually when you buy something, you're asked whether your credit card number, 
phone number or answer to your most secret question is still correct. However, 
since someone could look over your shoulder, you don't want that shown on your 
screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four 
characters into '#'.
"""
# return masked string
def maskify(cc):
    if len(cc) < 4:
        return cc
    
    cc = ("#" * (len(cc) - 4)) + cc[len(cc) - 4:len(cc)] 
    return cc

print(maskify("absdcabc")) 