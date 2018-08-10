#!/usr/bin/env python3
# -*- coding: utf-8 -*-
students = {
        "male":["Tom", "Hardy", "Brady", "Jenkins"],
        "female":["Maria", "Juliana", "Josefa", "Pepita"]
        }

for key in students:
    for name in students[key]:
        if "a" in name:
            print(name)

#name is a parameter that you give it. It can be anything, cows, shit