#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:40:01 2018



Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.

@author: marcus
"""

def fib(limit):
    lst = []
    lst.append(1)
    lst.append(2)
    
    while lst[-1] < limit:
        lst.append(lst[-2] + lst[-1])
    return lst[:-1]



limit = 4e6
seq = fib(limit)

res = 0
for nr in seq:
    if nr % 2 == 0:
        res += nr

print('Answer: ', res)