#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:48:31 2020

@author: ronaksharma
"""

#-------------- GREEDY ALGORITHMS-------------#
# 1. Dynamic Programming is also called memoisation. ou can dictionaries to store thigns
# especiialy for recursion cases like in fibonacci
#----1--Minimum Absolute Difference in an Array------#
#def minimumAbsoluteDifference(arr):
#    arr=sorted(arr)
#    minimumValues=1000000000
#    for i in range(len(arr)-1):
#        difference=abs(arr[i]-arr[i+1])
#        if(difference<minimumValues):
#            minimumValues=difference
#    return minimumValues
#    
#arr=[-2,2,4]
#result=minimumAbsoluteDifference(arr)
#print(result)

#----------2--Luck Balance---------------#
#def luckBalance(k, contests):
#    lossesAllowed=k
#    important=[]
#    unimportant=[]
#    countImportant=0
#    for i in contests:
#        if(i[1]==1):
#            countImportant+=1
#            important.append(i[0])
#        else:
#            unimportant.append(i[0])
#    numberOfWinsRequired=countImportant-lossesAllowed
#    summation2=sum(unimportant)
#    important=sorted(important)
#
#    if(numberOfWinsRequired>0):
#        summation3=sum(important[0:numberOfWinsRequired])
#        summation1=sum(important[numberOfWinsRequired::])
#    else:
#        summation3=0
#        summation1=sum(important)
#        
#    luckBalance=summation1+summation2-summation3
#    return luckBalance


#contests=[[5, 1], [4, 0], [6, 1], [2, 1], [8, 0]]
#k=2
#result=luckBalance(k,contests)
#print(result)

#------------3----Greedy Florist---------#
#def getMinimumCost(k, c):
#    numberOfFlowers=len(c)
#    c=sorted(c,reverse=True)
#    summation=0
#    count=1
#    counter=0
#    distanceLeft=numberOfFlowers-counter
#    while distanceLeft>=0:
#        if distanceLeft<k:
#            summation=summation+(sum(c[counter:]))*count
#        else:
#            summation=summation+(sum(c[counter:counter+k]))*count
#        count+=1
#        counter+=k
#        distanceLeft=distanceLeft-k
#    return summation
#    
#k=3
#c=[1,3,5,7,9]
#result=getMinimumCost(k,c)
#print(result)

#--------4-------Max Min-----------------#
#def maxMin(k, arr):
#    arr=sorted(arr)
#    i=0
#    minimumValue=(arr[k-1])-(arr[0])
#    while k+i<len(arr)+1:
#        calculate=(arr[k+i-1]) - (arr[i])
#        if(calculate<minimumValue):
#            minimumValue=calculate
#        i+=1
#    return minimumValue
#    
#
#k=3
##arr=[1,4,7,2]
#arr=[100
#,200
#,300
#,350
#,400
#,401
#,402
#]
#result=maxMin(k,arr)
#print(result)