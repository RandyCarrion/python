#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 08:49:45 2018

@author: randycarrion
"""
#get sentence from user
original = input("Sentence: ").strip().lower()


#split sentence into words

words = original.split()

#Loop through words and convert into pigLatin

latin = []
for pig in words:
    if pig[0] in "aeiou":
        new_word = pig + "yay"
        latin.append(new_word)
    else:
        vowel_pos = 0
        for letter in latin:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        const = pig[:vowel_pos]
        rest = pig[vowel_pos:]
        new_word = rest + const + "ay"
        latin.append(new_word)
print(latin)

#Stick words back together

pig_latin = "-fucker-".join(latin)

#output final string

print(pig_latin)