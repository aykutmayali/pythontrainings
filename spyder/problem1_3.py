# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 00:19:50 2021

@author: amayali
"""


def problem1_3(n):
    my_sum = 0
    i = 0
    while n >= 0 :        
        my_sum = my_sum + i
        i += 1
        n -= 1
    print(my_sum)    