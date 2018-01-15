# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:46:52 2018

@author: georg
"""
def chunks(l, n):
    chunks = []
    for i in range(0, len(l), n):
        if i + n <= len(l):
            for x in range(0, 3):
                chunk = (l[i + x:i + x + n])
                if len(chunk) == 3:
                    chunks.append(chunk)

    return chunks

def parity_matches(numbers):
    
    if (numbers[0] % 2 == 0 and numbers[1] % 2 == 0 and numbers[2] % 2 == 0) \
    or \
    (numbers[0] % 2 == 1 and numbers[1] % 2 == 1 and numbers[2] % 2 == 1):        
        return True
    
    return False

    
def three_amigos(numbers):
    r_min = float('inf')
    chuncked = []
    chuncked = chunks(numbers, 3)
    
    for elem in chuncked:
       if(parity_matches(elem)):
           r_range = (max(elem) - min(elem))
           if r_range < r_min:
               r_min = r_range
               to_return = elem
               
    
    return to_return
    

print (three_amigos([0, -1, -1, 1, -1, -1, -3]))

