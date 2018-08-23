#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:32:09 2018

Problem: 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: marcus
"""

import numpy as np

limit = 1000

three = np.arange(0, limit, 3)
five = np.arange(0, limit, 5)
fifteen = np.arange(0, limit, 15)
ans = np.sum(three) + np.sum(five) - np.sum(fifteen)
print(ans)
