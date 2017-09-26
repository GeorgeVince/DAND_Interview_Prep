# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:40:00 2017

@author: georg

Task

Write a function deNico/de_nico() that accepts two parameters:

    key/$key - string consists of unique letters and digits
    message/$message - string with encoded message

and decodes the message using the key.

First create a numeric key basing on the provided key by assigning each letter 
position in which it is located after setting the letters from key in an 
alphabetical order.

For example, for the key crazy we will get 23154 because of acryz 
(sorted letters from the key).
Let's decode cseerntiofarmit on using our crazy key.

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n

After using the key:

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n

Notes

    The message is never shorter than the key.
    Don't forget to remove trailing whitespace after decoding the message

Examples

deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key"

"""

def de_nico(key,msg):   

    key_vals = ["".join(sorted(key)).find(key[i]) for i in range(0, len(key))]
    chunked = [msg[i:i + len(key)] for i in range(0, len(msg), len(key))]
    
    to_return = ""
    
    for part in chunked:
        for idx in key_vals:
            if idx < len(part):
                to_return += part[idx]

    return to_return.strip()

#print(de_nico("crazy", "cseerntiofarmit on  "))
print(de_nico("vligds","letcfvlmebegkxvjgjftb"))
#vctelfgbemlejjvxkgftb
#vctelfgbemlejjvxkgbtf