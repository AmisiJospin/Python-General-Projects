# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:35:06 2021

@author: Jospin Amisi
"""

"""
Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because [mathjaxinline]1*10^3+2*10^2+3*10^1+4*10^0[/mathjaxinline].

"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def to_apply (x):
        n = 0
        for i in L:
            n = x*n + i
        return n
    return to_apply