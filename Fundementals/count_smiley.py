# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:03:26 2017

@author: georg

Given an array (arr) as an argument complete the function countSmileys 
that should return the total number of smiling faces.

Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :]
"""

    
def count_smileys(arr):
    counter = 0
    for face in arr:
        if face[0] == ";" or face[0] == ":":
            if (len(face) == 3) and (face[1] == "-" or face[1] == "~") and \
            (face[2] == ")" or face[2] == "D"):
                counter += 1
            elif (len(face) == 2) and (face[1] == ")" or face[1] == "D"):
                counter += 1

    
    return counter
    
                

        
    
    
               



print (count_smileys([':)',':(',':D',':O',':;']))
