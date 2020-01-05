#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:39:49 2020

@author: snk
"""

# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# chars 6 
# Digits 2

s = input("Enter input string")

digits= chars =0

for i in s:
    #check is char is digit
    if i.isdigit():
        digits = digits +1
        
    #check char is letter 
    elif i.isalpha():
        chars =chars + 1
    
    #other than letter or digits
    else:
        pass
   
print("letters: ", chars)
print("digits: ", digits)
    

        