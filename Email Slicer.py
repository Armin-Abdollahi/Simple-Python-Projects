#!/usr/bin/env python
# coding: utf-8

# In[ ]:


email = input("Enter your email address: ")

# Find the index of the "@" symbol
at_index = email.index("@")

# Slice the username and domain name from the email address
username = email[:at_index]
domain = email[at_index+1:]

# Print the username and domain name
print("Username:", username)
print("Domain:", domain)

