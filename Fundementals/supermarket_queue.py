# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:49:31 2017

@author: georg

There is a queue for the self-checkout tills at the supermarket. Your task is 
write a function to calculate the total time required for all the customers to 
check out!

The function has two input variables:

    customers: an array (list in python) of positive integers representing the 
    queue. Each integer represents a customer, and its value is the amount of 
    time they require to check out.
    n: a positive integer, the number of checkout tills.

The function should return an integer, the total time required.

EDIT: A lot of people have been confused in the comments. To try to prevent 
any more confusion:

    There is only ONE queue, and
    The order of the queue NEVER changes, and
    Assume that the front person in the queue (i.e. the first element in the array/list) 
    proceeds to a till as soon as it becomes free
"""



def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    
    
    tills = [0] * n
    #Populate tills
    for i in range(0, n):
        if customers == []:
            break
        else:
            tills[i] = customers.pop(0)

    counter = 0
    while sum(tills) != 0:
        
        for i in range(0, n):
            if tills[i] > 0:
                tills[i] -= 1
            
            if tills[i] == 0 and len(customers) > 0:
                tills[i] = customers.pop(0)
                
        counter += 1

    return (counter)
    # TODO
    
print (queue_time([2,2,3,3,4,4,1], 2))