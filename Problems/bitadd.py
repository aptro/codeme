# -*- coding: utf-8 -*-
#Add two numbers without using arithmetic operators

#If x and y don’t have set bits at same position(s), 
#then bitwise XOR (^) of x and y gives the sum of x and y. 
#To incorporate common set bits also, bitwise AND (&) is used. 
#Bitwise AND of x and y gives all carry bits. 
#We calculate (x & y) << 1 and add it to x ^ y to get the required result.

def add(x, y):
    if y ==0:
        return x
    else:
        return add(x^y, (x&y)<<1)