#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:42:11 2020

@author: ronaksharma
"""

#--------- SORTING-----------#

#--1-----Bubble Sort----#
# 1. TWO LOOPS: ONE ACTUALLY BUBLLE SORTS AND SWAPS, THE BIG ONE JUST REPEATS N TIMES
# 2. SWAP: INITIALISE THAT IT IS SORTED. IF THERE IS SWAP THEN SET TO SRTED=FALSE AS NOT SORTED YET
# 3. IF THERE IS NO SWAP IN A SINGLE BUBBLE SORT SEARCH(I.E. LOOP J) THEN SORTED

#def countSwaps(a):
#    n=len(a)
#    swap=0
#    for i in range(n):
#        isSorted=True
#        for j in range(n-i-1):
#            if(a[j]>a[j+1]):
#                a[j],a[j+1]=a[j+1],a[j]
#                swap+=1
#                isSorted=False

#        if(isSorted==True):
#            print("Array is sorted in",swap,"swaps.")
#            print("First Element:",a[0])
#            print("Last Element:",a[n-1])
#            break
#            
#
#
#a=[3,2,1]               
#countSwaps(a)

#--2-------QUICK SORT-------#
# 1. CHOOSE PIVOT. ALL VALUES LESS BE ON LEFT array AND ALL VALUE GREATER BE ON RIGHT array
# 2. FIND A BIGGER VALUE ON LEFT AND SMALLER ON RIGHT AND THEN SWAP THEM
# Best case O(n, worst case O(n2)

#from random import randint
#def quicksort(array):
#    if len(array)<2:
#        return array
#    
#    low, same, high = [], [], []
#    pivot = array[randint(0, len(array) - 1)]
#    for item in array:
#        if(item<pivot):
#            low.append(item)
#        elif(item==pivot):
#            same.append(item)
#        elif(item>pivot):
#            high.append(item)
#
#            
#    return quicksort(low)+same+quicksort(high)
#    
#arr=[5,4,7,3,6,1]
#result=quicksort(arr)
#print(result)

#-3------ SORTED COMPARATOR----------#
# Use to sort lists of lists using a logic you have created. It tells the
# function if that particular element is bigger than or less than the comparing element
# sorted will use merge sort with your logic

#---------Lambda Function as Comparator----------#
# 1. Much easier to implement and understand than key_cmp...
# 2. Below shows two ways it can be used to sort arrays
#arr=[(1,2,3),(-1,2,4),(4,3,-4),(4,5,3)]
#arrNew=sorted(arr,key=lambda arr:sum(arr)) # Sorts the tuples with smallest sum
#print(arrNew)
#
#arr=[[1,3],[2,-1],[3,2]]
#arrNew=sorted(arr,key=lambda arr:arr[1]) # Sorts by second index of the list
#print(arrNew)
#
#animals = [     {'type': 'penguin', 'name': 'Stephanie', 'age': 8},    {'type': 'elephant', 'name': 'Devon', 'age': 3},    {'type': 'puma', 'name': 'Moe', 'age': 5}, ]
#sorted(animals, key=lambda animal: animal['age']) # Sorts by the value of key 'age'
#----------------------------------#



#from operator import itemgetter # decide the index of the array to sort stuff by
#from operator import attrgetter # define the type of object you want sort by
#from functools import cmp_to_key
#
##----- Below is example of a custom operator--------#
#def compare(a,b):
#    if(sum(a)>sum(b)):
#        return 1
#    elif(sum(a)<sum(b)):
#        return -1
#    else:
#        return 0
#        
#tuple_test = [[1,2,3],[3,4,5],[5,6,7,7],[3,3,4,4],[3,4,5],[1]]
#compareResult=sorted(tuple_test, key=cmp_to_key(compare), reverse=False)
#print(compareResult)





#----4---MAKING TOYS----#
#def maximumToys(prices, k):
#    summation=0
#    counter=0
#    prices.sort()
#    for i in prices:
#        summation=summation+i
#        if(summation<=k):
#            counter+=1
#        elif(summation>k):
#            break
#        else:
#            None
#    return counter
#
#prices=[1 ,12, 5 ,111, 200, 1000, 10]
#k=50
#result=maximumToys(prices,k)
#print(result)
    
    
#----5--------MERGE SORT---------#

#Brute Force Version1#
#def countInversions(arr):
#    counter=0
#    for i in range(len(arr)):
#        for j in range(i,len(arr)-1):
#            if(arr[i]>arr[j+1]):
#                counter+=1
#    return counter
#    
#arr=[2,1,3,1,2]
#result=countInversions(arr)
#print(result)
    
#Optimised Version 1#
# 1. Think of Stopping Condition
# 2. What to do when not stopping
# 3. Calling two recurssions at a time will call two functions remember
# O(nlogn) is always. Not good for sorting small lists. Then bubble or insertion better
#counter=0
#def countInversions(arr):
#    counter=0
#    leftStart=0
#    rightEnd=len(arr)-1
#    temp=[None]*len(arr)
#    mergeSort(arr,temp,leftStart,rightEnd)
#    return counter
#    
#def mergeSort(arr,temp,leftStart,rightEnd):
#    if(leftStart>=rightEnd):
#        return
#        
#    midVal=int((leftStart+rightEnd)/2)
#    mergeSort(arr,temp,leftStart,midVal)
#    mergeSort(arr,temp,midVal+1,rightEnd)
#    mergeHalves(arr,temp, leftStart,rightEnd)
#
#def mergeHalves(arr,temp,leftStart,rightEnd):
#    global counter
#    leftEnd=int((leftStart+rightEnd)/2)
#    rightStart=leftEnd+1
#    
#    left=leftStart #Otherise set to zero everytime and will forget eth index when recursion is over
#    right=rightStart
#    index=leftStart
#    
#    while(left<=leftEnd and right<=rightEnd):
#        if(arr[left]<=arr[right]):
##            print(arr[left],arr[right])
#            temp[index]=arr[left]
#            left=left+1
#            
#        else:
#            temp[index]=arr[right]
##            print(arr[left],arr[right])
##            print(temp)
#            swaps=right-index
#            counter+=swaps
#            right=right+1
#
#        
#        index=index+1
#        
#    while(index<=rightEnd and right<=rightEnd):
#        temp[index] = arr[right]
#        right += 1
#        index += 1
#        
#    while(index<=rightEnd and left<=leftEnd):
#        temp[index] = arr[left]
#        left += 1
#        index += 1
#        
#    for i in range(leftStart,rightEnd+1):
#        arr[i] = temp[i]

#    
#arr=[2,1,4,5,3]
#arr2=[7,5,3,1]
#arr3=[1,1,1,2,2]
#arr4=[3,2,1]
#result=countInversions(arr2)
#print(result)
    
#------------- Revision-----------#
def quicksort(arr):
    if(len(arr)<2):
        return arr
    else:
        low,high,same=[]
        pivot=arr[l+r//2]
    for i in arr:
        if(i<pivot):
            low.append(i)
        elif(i>pivot):
            high.append(i)
        else:
            same.append(i)
    return quicksort(low)+same+quicksort(high)
    
    
def merge(arr,leftStart,righEnd):
    if(leftStart>=righEnd):
        return
    else:
        mid=leftStart+righEnd//2
        merge(arr,leftStart,mid)
        merge(arr,mid+1,righEnd)
        mergehalves(arr,leftStart,righEnd)
    
def mergehalves(arr,leftStart,rightEnd):
    mid=rightEnd+leftStart//2
    leftEnd=mid
    rightStart=mid+1
    left=leftStart
    right=rightStart
    index=leftStart 
    temp=[]
    while(left<=leftEnd and right<=rightEnd):
        if(arr[left]<arr[right]):
            left+=1
            temp[index]=arr[left]
        else:
            temp[index]=arr[right]
            right+=1
        index+=1
   
    while(index<=rightEnd and right<rightEnd):
        temp[index]=arr[right]
        right+=1

    while(index<leftEnd and left<leftEnd):
        temp[index]=arr[left]
        left+=1
    
    for i in range(arr):
        arr[i]=temp[i]
    
    
    
    
    
    
    
    
    
    
    
    
    


