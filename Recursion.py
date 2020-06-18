#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:01:21 2020

@author: ronaksharma
"""

#--------- RECURSION-------#
# 1. Always have a stopping condition
# 2. Recursion is like solving sub problems

#---1. Fibonnaci------#
#def fibonacci(n):
#    if n==0 or n==1:
#        return n
#    else:
#        sumOfElements=fibonacci(n-1)+fibonacci(n-2)
#        
#    return sumOfElements
#    
#
#n=5
#result=fibonacci(n)
#print(result)

#------2. Staircase-------#
#def stepPerms(n):
#    mod=10000000007
#    s=calculate(n,mod)
#    return s
#    
#listOf=dict()
#def calculate(n,mod):
#    global listoF
#    if(n in listOf.keys()):
#        return listOf[n]
#    elif n<0:
#        return 0
#    elif(n==0):
#        return 1
#    else:
#        stepSize1=calculate(n-1,mod)
#        stepSize2=calculate(n-2,mod)
#        stepSize3=calculate(n-3,mod)
#        totalStepSize=(stepSize1)+(stepSize2)+(stepSize3)
#        listOf[n]=totalStepSize%mod
#    return listOf[n]

#n=7 
#result=stepPerms(n)
#print(result)
#print(listOf)


#---------------DYNAMIC PROGRAMMING------------#
#listOfVisited=[None]*(n+1)
##---1. Fibonnaci------#
#def fibonacci(n):
#    global listOfVisited
#    if(listOfVisited[n]!=None):
#        return listOfVisited[n]
#    elif n==0 or n==1:
#        return n
#    else:
#        sumOfElements=fibonacci(n-1)+fibonacci(n-2)
#        listOfVisited[n]=sumOfElements
#    return sumOfElements
#    
#
#n=6
#result=fibonacci(n)
#print(result,listOfVisited)



#----- Max Array Sum-------#
#------ FAILS DUE TO TIMEOUT
#def maxSubsetSum(arr):
#    n=len(arr)
##    listOfSubstrings=[]
#    maxVal=-10000
#    for i in range(len(arr)):
#        for j in range(1,len(arr)):
#            if(j+1>=n-i):
#                break
#            else:
#                summation=sum(arr[i::j+1])
#                if(summation>maxVal):
#                    maxVal=summation
##                listOfSubstrings.append(arr[i::j+1])
#    
#    return maxVal
#
#------Using DP--------#
#def maxSubsetSum(arr):
#    maxList=[]
#    maxList.append(arr[0])
#    if(arr[1]>arr[0]):    
#       maxList.append(arr[1])
#    else:
#        maxList.append(arr[0])
#    for i in range(2,len(arr)):
#        value1=arr[i]+maxList[i-2]
#        value2=arr[i]
#        value3=maxList[-1]
#        maximumValue=max(value1,value2,value3)
#        maxList.append(maximumValue)
#        
#    return maxList[-1]
#
#arr=[2,1,5,8,4]
#s=maxSubsetSum(arr)
#print(s)

#------Number of Handshakes problem-----#
# Take example of H(4)=H(3)+3
# Number of handshkes 3 people will take plus if another person is there
# the there will be 3 extra handshakes, as 3 peopel will shake hand with that
# one person
        
#--------String Permutation---------#
# 1. A string of length n has n! permuataions
# Here 'left'defines the position of the fixed character
# All possible permutations are generated at the end of the recursion, so don't
# need to count anything in the middle
#sumation=0
#def permute(arr,left,right):
#    global sumation
#    if(left==right): # This means nothing left to swap. Fixed all cases
#        print(''.join(arr))
#        sumation=sumation+1
#    else:
#        for i in range(left,right):
#            a[left],a[i]=a[i],a[left]
#            permute(arr,left+1,right)
#            a[i],a[left]=a[left],a[i]
#    return sumation
#string = "ABC"
#n = len(string) 
#a = list(string) 
#result=permute(a,0,n)
#print(result)     
        
#-------------Palindrone--------#
# Checking Palindrone using the concept of recursion
# 1. Instead of checking, check if not a palindrone as then can break

#def first(word):
#    return word[0]
#
#def last(word):
#    return word[-1]
#
#def middle(word):
#    return word[1:-1]
#
#def is_palindrone(testString):
#    if(len(testString)<3):
#        return True
#    else:
#        if(first(testString)==last(testString)):
#            middleString=middle(testString)
#            result=is_palindrone(middleString)
#        else:
#            return False
#    return result
#    
#p="allen"
#outcome=is_palindrone(list(p))
#print(outcome)
    
#--------Memoisation Example=--------#
# 1. Always store the return statement in the dictionary and then return the dictionary
# Ex-11.2 Think Python
#def ackermann(m, n):
#    d=dict()
#    if (m,n) in d:
#        return d[(m,n)]
#    if m == 0:
##        d[(m,n)]=n+1 Not needed here as every statemetn goes to the return at the end
#        return n+1
#    if n == 0:
##        d[(m,n)]=ackermann(m-1, 1) Not needed here as every statemetn goes to the return at the end
#        return ackermann(m-1, 1)
#    d[(m,n)]=ackermann(m-1, ackermann(m, n-1))
#    return d[(m,n)]
#
#print(ackermann(3, 4))






















        
        
        
        