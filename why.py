#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import choice

questions = [
        "Why is the moon white?: ",
        "Where am I?: ",
        "Why brown?: ",
        "Where are the real people?: ",
        "Why is the eye round?: "
        ]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
    
print("Oh...Okay")