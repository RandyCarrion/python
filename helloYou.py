#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Ask user for name
#name = input("What is your name?: ")

#Ask user for age
#age = int(input("How old are you?: "))


#Ask user for city
#city = input("What city do you live in?: ")

#Ask user what they enjoy
#love = input("what do you love doing?: ")

#Create output text
#string = 'Your name is {} and you are {} years old. You live in {} and love doing {}.'
#output = string.format(name, age, city, love)
#.format fills in info within other variables wherever you put them. 
#You hasve to put them in another variable than the string itself...
#Print output on screen

#print(output)

start = "I am"
age = int("27")
end = "years old"
string = "{} {} {}".format(start, age, end)
print(string)