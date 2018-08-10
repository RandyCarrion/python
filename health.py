#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
random.randint(25, 50)
health = 50

difficulty = 3 
 

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health
print(health)