#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:38:04 2020

@author: ronaksharma
"""

#-------- STACKS AND QUEUES--------#
# 1. Search and Space complexity is O(n)
# 2. Inserting or Deletion is O(1)

#-----1. Balanced Brackets--------#
#def isBalanced(s):
#   left_brackets=['{','[','(']
#   right_brackets=['}',']',')']
#   counter=0
#   closureList=[]
#   for i in s:
#       if i in right_brackets:
#           counter+=1
#       if i in left_brackets:
#           closureList.append(i)
#       else:
#           if(len(closureList)!=0):
#               topElelment=closureList.pop()
#               if(i=='}'):
#                   if(topElelment!='{'):
#                       return "NO"
#                   else:
#                       counter=counter-1
#               elif(i==')'):
#                   if(topElelment!='('):
#                       return "NO"
#                   else:
#                       counter=counter-1
#               elif(i==']'):
#                   if(topElelment!='['):
#                       return "NO"
#                   else:
#                       counter=counter-1
#   if(len(closureList)==0) and counter==0:    
#       return "YES"
#   else:
#       return "NO"
#   
#   
#s="]]"
#result=isBalanced(s)           
#print(result) 