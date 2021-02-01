# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 00:22:02 2021

@author: amayali
"""


def problem1_7():
    b1 = input("Enter the length of one of the bases:")
    b2 = input("Enter the length of the other base:")
    h = input("Enter the height:")
    f_b1 = float(b1)
    f_b2 = float(b2)
    f_h = float(h)
    a = (f_b1+f_b2)*f_h*.5
    print("The area of a trapezoid with bases",f_b1,"and",f_b2,"and height",f_h,"is",a)