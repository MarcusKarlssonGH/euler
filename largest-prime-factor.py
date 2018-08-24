#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:54:12 2018



The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


@author: marcus
"""


#number = 13195
number = 600851475143

def find_factors(number, factors = []):
    div = 2
    while number % div:
        div += 1
    factors.append(div)
    if div == number:
        return factors
    else:
        return find_factors(number / div, factors)


factors =  find_factors(number)
print('Answer: ', factors[-1])



                                               