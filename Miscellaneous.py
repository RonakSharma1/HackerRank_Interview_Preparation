#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:44:59 2020

@author: ronaksharma
"""

#--------------Time Complexity: Primality----------#
# 1. Brek whenrver you see a prime,so always start the loop not counting 1 and the number itself
#def primality(n):
#    x="Prime"
#    count=0
#    n2=int(math.sqrt(n))
#    if(n<2):
#        x="Not prime"
#    elif(n==2):
#        x="Prime"
#    elif(n%2==0 or n%3==0):
#        x="Not prime"
#    else:
#        for i in range(3,n2+1):
#            if(n%i==0):
#                x="Not prime"
#                break
#    return x
#
#    
#n=4
#result=primality(n)
