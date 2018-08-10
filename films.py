#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:15:43 2018

@author: randycarrion
"""

films = {
        "Finding Dory": [3,5],
        "Bourne": [18, 5],
        "Tarzan": [15,5],
        "Ghostbusters": [12,5]
        }

while True: 
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        
        age = int(input("What is your age?: ").strip())
        
        if age >= films[choice][0]:
            
            num_seats = films[choice][1]
            
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] -1
            
            else:
                print("Sorry, sold out!")
        
        else:
            print("You're too young to watch the film, sorry")
    
    else:
        print("We dont have that film")