# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:20:53 2018

@author: georg
"""


def scramble_word(word):
    print (word)
    non_letters = {}
    to_sort = []
    
    if len(word) < 3:
        return word
    
    to_sort = ''.join([i for i in word if i.isalpha()])
    
    
    for i, c in enumerate(word):
         if not c.isalpha():
             non_letters.update({i:c})
      
    word = to_sort[0] + ''.join(sorted(to_sort[1:-1])) + to_sort[-1]
    
    word_list = list(word);
    for key, value in non_letters.items():
            word_list.insert(key, value)
      
    to_return = ''.join(word_list)
     
    print (to_return)
    return to_return
        
    


def scramble_words(words):
    
    to_return = ''
    for word in words.split():
        to_return = to_return + scramble_word(word) + " "
    return to_return[0:-1]

    
print (scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."))
