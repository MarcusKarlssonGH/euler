#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:54:15 2018


2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?


@author: marcus
"""

import math

number = 20
for factor in range(19, 0, -1):
    number *= factor //  math.gcd(number, factor)
    
print('Answer: ', number)