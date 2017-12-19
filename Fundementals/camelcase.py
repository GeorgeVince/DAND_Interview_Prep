# -*- coding: utf-8 -*-
"""
 camelCase 1: The first letter of each word should be capitalized. 
               Except for the first word.

 Example: "Hello world"  -->  "helloWorld"

 camelCase 2: The last letter of each word should be capitalized. 
               Except for the last word. 

 Example: "Hello world"  -->  "hellOworld"

 camelCase 3: The first and last letters of each word should be capitalized. 
               Except for the first and lasts letter of sentence. 

 Example: "Hello world"  -->  "hellOWorld"
"""

def upperfirst(x):
    x = x.lower()
    return x[0].upper() + x[1:]

def upperLast(x):
    return x[0:len(x) - 1].lower() + x[len(x) - 1].upper()

def upperFirstAndLast(x):
    return x[0].upper() + x[1:-1].lower() + x[-1].upper()

def toCamelCase(s, n):
    toReturn = ""
    words = s.split()
    
    if n == 1:
        toReturn += words[0].lower()
       
        for word in words[1:]:
            toReturn += upperfirst(word)
    
    elif n == 2:       
        for word in words[0:len(words) - 1]:
            toReturn += upperLast(word)
        toReturn += words[-1].lower()
        
    elif n == 3:
        toReturn += upperLast(words[0])
       
        for word in words[1:len(words) - 1]:
            toReturn += upperFirstAndLast(word)
            
        toReturn += upperfirst(words[-1])
        
    return toReturn
        

print (toCamelCase("xWGGGN KYKG kmQLmA IxKFWgE JoCEyxD vLFi", 3))

#print(upperLast("world"))