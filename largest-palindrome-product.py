#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:53:09 2018


A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


@author: marcus
"""

def extract_digits(number):
    return [int(digit) for digit in str(number)]

def is_palindrome(lst):
    for idx, element in enumerate(lst):
        if element != lst[-(idx+1)]:
            return False
    return True

res = 0
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        number = num1*num2
        if is_palindrome(extract_digits(number)):
            res = max(res, number)
        
print('Answer: ', res)