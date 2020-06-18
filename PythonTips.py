#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:28:50 2020

@author: ronaksharma
"""

#------------- GENERAL PYTHON TIPS---------------#

#------ Enumeration-----#
#arr=[3,4,5,6,23]
#for i, num in enumerate(arr,start=2):
#    print(i,num)# Here i is just a counter, not related to the index of the arr

#-----List Comprehension-----#
# 1. Can be much faster than for loops in some instances
#arr=[1,2,4,-1,-2,4]
#def square(x):
#    return x**2
#def isNegative(x):
#    if(x<0):
#        return 1
#    else:
#        return 0
#        
#arr_square=[square(x) for x in arr] # First teh right part after 'For' is executed
#print(arr_square)                   # then square(x) is called for each x
#arr_isNegative=[arr.index(i) for i in arr if(isNegative(i))]
#print(arr_isNegative)

#------ Debugging----------#
# Pauses the programme in where inserted and allows to interact with shell to get
# values of variables or list or any other parameters
#import pdb
#arr=[1,2,3,4,5,6,7,8,9]
#arr=arr[0:7]
#pdb.set_trace() # This is the debugger
#arr=arr[0:3]

#------------ Itertools-----------------#
# 1. Combinationa and Permutations creates all possible groups of elements, so essentially SubArrays
#import itertools
#x=['Ronak','Rajiv','Renu','Raghu']
#y1=list(itertools.combinations(x,r=3)) # Order matter
#y2=list(itertools.permutations(x,r=3)) # Order does not matter
#
#print(y1)
#print(y2)

#----------- Regular Expression--------#

