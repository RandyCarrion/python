#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:11:18 2018

@author: randycarrion
"""

users = ["Alice", "Randy"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    
    if name in users:
        print("Hi,",name,".")
        remove = input("Would you like to stay on the list? (y/n): ").strip().lower()
        if remove == "y":
            print("I'm glad you like us ", name , "!")
        elif remove == "n":
            users.remove(name)
            print("Bye ",name , ".")
            
            
    else:
        add = input("Name not recognised. Would you like to join us? (y/n): ").strip().lower()
        if add == "y":
            users.append(name)
            print("You are added to the list!" ,name)
        elif add == "n":
            print("Bye Shaniqua!")
        print(users)