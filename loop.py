#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:50:07 2018

@author: randycarrion
"""
L = []

while len(L) <2:
    new_name = input("Name: ").strip().capitalize()
    L.append(new_name)
    
print("sorry, list is full")
print(L)
