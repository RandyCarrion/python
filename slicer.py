#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#get user email
email = input("What is your email?: ").strip()

#slice out username
user = email[:email.index("@")].upper()

#slice domain name
domain = email[email.index("@") + 1 :]

#format message
output = "Your username is {} and your domain is {}".format(user, domain)

#display output message
print(output)
