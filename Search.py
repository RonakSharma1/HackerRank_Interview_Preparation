#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:58:22 2020

@author: ronaksharma
"""
# 1. For a Sorted array of Unknown size, use BS to first get the size of array
# by finding the last element in the array. Then another BS to find the required element
# Each time a[mid]<num
#---------------SEARCH----------#

#Example 1:Binary Search#
# 1. Divide and conquer but ensure that it is a sorted array
# 2. Binary Search on 2D array
# 3. ALWAYS HAVE AN ELSE OTHERWISE WILL GET STUCK
#def binarySearch(array,left,right,val):
#    while(left<=right):
#        middle=left+int((right-left)/2)
#        if(array[middle][0]==val):
#            return array[middle][1]
#        elif(val<array[middle][0]):
#            right=middle-1
#        elif(val>array[middle][0]):
#            left=middle+1
#    
#array=[[2,2],[2,0],[3,1],[4,3]]
#left=0
#right=len(array)-1
#val=2
#result=binarySearch(array,left,right,val)
#print(result)

# Example 2: First Value Greater than Target
#def binarySearch(array,left,right,val):
#    ans=-1
#    while(left<=right):
#        middle=left+int((right-left)/2)
#        if(array[middle]>=val):
#            ans=middle
#            right=middle-1
#        else:
#            left=middle+1
#    return array[ans]

# Example 3: Maximum Value in the Rotated Array
#def binarySearch(array,left,right):
#    ans=-1
#    while(left<=right):
#        middle=left+int((right-left)/2)
#        if(array[middle]>=array[middle-1]) :
#            ans=middle
#            left=middle+1
#        else:
#            right=middle-1
#    return array[ans]
#    
#array=[2,4,5,7,10,12,20,11,12]
#left=0
#right=len(array)-1
#result=binarySearch(array,left,right)
#print(result)

# Example 4: Binary Search using Integer Values for SQRT
#def binarySqrt(left,right,val):
#    while(abs(left-right)>0.001):
#        middle=left+((right-left)/2)
#        if(middle*middle<val):            
#            left=middle
#        else:
#            right=middle
#    return middle
#    
#val=4
#left=0
#right=val
#result=binarySqrt(left,right,val)
#print(result)

#Problem1 : Ice Cream Parlor#
# 1. Always have an else otherwsie time out
# 2. Binary Search is possible in 2D Array
# 3. ALWAYS SORT THE ARRAY BEFORE BINARY SEARCH
#def whatFlavors(cost, money):
#    #Sort using Comparator
#    x=-1
#    y=-1
#    costArray=[]
#    for i in range(len(cost)):
#        costArray.append([cost[i],i])
#    
#    costArray.sort()
#    for i in range(len(costArray)):
#        money_required=money-costArray[i][0]
#        result=binarySearch(costArray,i+1,len(costArray)-1,money_required)
#        if(result!=None):
#            x=min(costArray[i][1]+1,result+1)
#            y=max(result+1,costArray[i][1]+1)
#            break
#    print(x,y)
#    
#def binarySearch(array,left,right,val):
#    while(left<=right):
#        middle=left+int((right-left)/2)
#        if(array[middle][0]==val):
#            return array[middle][1]
#        elif(val<array[middle][0]):
#            right=middle-1
#        else:
#            left=middle+1
#    
#money=12
#cost=[7,2,5,4,11]
#result=whatFlavors(cost,money)

#----- Count number of occurences--------#
# 1. Method 1: Find the occurence of x using BS and count the number of elements
# to its left and then to its right. Thats the total count
# 2. Method 2: Using BS, find the first occurence of the element i.e.
# First Occurence (arr[mid-1]<x or mid==0) and (arr[mid]==x)
#  Last Occurence (mid==n-1 or arr[mid+1]>x)and(arr[mid]==x)
#def firstOccurence(arr,l,r,val):
#    while(l<=r):
#        mid=l+int((r-l)/2)
#        if((arr[mid-1]<val or mid==0) and arr[mid]==val):
#            return mid
#        elif(arr[mid]<val):
#            l=mid+1
#        else:
#            r=mid-1
#            
#arr=[1,2,3,3,4,5]
#result=firstOccurence(arr,0,6-1,3)
#print(result)

#-----4-------Swap Node Algo----------#
# 1. You can create and traverse the tree at the same time
   
#class Node:
#    def __init__(self,data):
#        self.data=data
#        self.right=None
#        self.left=None
#           
#                
#def traverse(root,val,children):
#    if root==None:
#        return
#    elif root.data==val:
#        if(children[0]!=-1):
#            root.left=Node(children[0])
#        if(children[1]!=-1):
#            root.right=Node(children[1])
#        return
#    else:
#        traverse(root.left,val,children)
#        traverse(root.right,val,children)
#  
#def swappingNodes(nodesToSwap):
#    for i in nodesToSwap:
#        if(i.left==None):
#            i.left=i.right
#            i.right=None
#        elif(i.right==None):
#            i.right=i.left
#            i.left=None
#        else:
#            i.left,i.right=i.right,i.left
#        
#def traverseToSwap(root,heightToSwap,heightOfTree,nodesToSwap):
#    if root==None:
#        return
#    else:
#        traverseToSwap(root.left,heightToSwap,heightOfTree+1,nodesToSwap)
#        if(heightOfTree%heightToSwap==0):
#            nodesToSwap.append(root)
#        traverseToSwap(root.right,heightToSwap,heightOfTree+1,nodesToSwap)
#    return nodesToSwap
#     
#def traverseToPrint(root,inOrderTraversal):
#    if root==None:
#        return
#    else:
#        traverseToPrint(root.left,inOrderTraversal)
#        inOrderTraversal.append(root.data)
#        traverseToPrint(root.right,inOrderTraversal)
#        
#def swapNodes(indexes, queries):
#    root=Node(1)
#    val=1
#    heightOfTree=1
#    nodesToSwap=[]
#    inOrderTraversal=[]
#    x=[]
#    for i in range(len(indexes)):
#        traverse(root,val,indexes[i])
#        val+=1
#    for heightToSwap in queries:
#        nodeList=traverseToSwap(root,heightToSwap,heightOfTree,nodesToSwap)
#        swappingNodes(nodeList)
#        nodesToSwap=[]
#        traverseToPrint(root,inOrderTraversal)
#        x.append(inOrderTraversal)
#        inOrderTraversal=[]
#    return x
#indexes=[[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
#queries=[2,4]
#result=swapNodes(indexes,queries)
#print(result)

#----5---------Pairs-----------------#
# BECAUSE NO DUPLICATES
# 1. Just check that for each integer N, does N+K pair exists or not
# So create a list of N+k pairs and do an intersection to find the common values
# 2. very good use of SETS**
#def pairs(k, arr):
#    a = set(arr)
#    # make a set of all a[i] + k
#    b = set(x + k for x in arr)
#    print(a,b)
#    # return the length of the intersection set
#    return len(a&b)
#------------OR----------------#
#def pairs(k, arr):
#    arr=sorted(arr)
#    countOfSolutions=0
#    for i in range(1,len(arr)):
#        left=i-1
#        right=len(arr)-1
#        findValue=arr[left]+k
##        print(findValue,arr[left],k)
#        while(left<=right):
#            mid=left+int((right-left)/2)
#            if(arr[mid]==findValue):
#                countOfSolutions+=1
##                print(arr[mid],arr[i])
#                break
#            elif(findValue>arr[mid]):
#                left=mid+1
#            else:
#                right=mid-1
#    return countOfSolutions


  
#arr=[1,5,3,4,2]
#k=2
#result=pairs(k,arr)
#print(result)

#------6---------Triple Sum-----------#

#------- Using Binary Search---------#
#def binarySearch(arr,targetVal):
#    left=0
#    right=len(arr)-1
#    index=1
#    if(targetVal>arr[right] or targetVal==arr[right]): # This condition pervents to perfrom binary search and return the solution in O(1)
#        return right+1
#    else:
#        while(left<=right):
#            mid=left+int((right-left)/2)
#            if(arr[mid]>targetVal):
#                index=mid
#                right=mid-1
#            else:
#                left=mid+1
#        return index

#def triplets(a, b, c):
#    cntInA=0
#    cntInC=0
#    tempProduct=0
#    finalScore=0
#    a=sorted(list(set(a)))
#    b=sorted(list(set(b)))
#    c=sorted(list(set(c)))
#    for i in range(len(b)):
#        
#        cntInA=binarySearch(a,b[i])
#        cntInC=binarySearch(c,b[i])
#                
#        tempProduct=cntInA*cntInC
#        finalScore=finalScore+tempProduct
#    return finalScore
#    
#a=[1,3,5,7]
#b=[5,7,9]
#c=[7,9,11,13]
#result=triplets(a,b,c)
#print(result) 


#--------------TIMES OUT-------------#
#def triplets(a, b, c):
#    cntInA=0
#    cntInC=0
#    tempProduct=0
#    finalScore=0
#    a=sorted(list(set(a)))
#    b=sorted(list(set(b)))
#    c=sorted(list(set(c)))
#    for i in range(len(b)):
#        for m in range(cntInA,len(a)):
#            if(a[m]<=b[i] and b[i]!=b[i-1]):    
#                cntInA+=1
#            
#        for n in range(cntInC,len(c)):
#            if(c[n]<=b[i] and b[i]!=b[i-1]):
#                cntInC+=1
#                
#        tempProduct=cntInA*cntInC
#        finalScore=finalScore+tempProduct
#    return finalScore
#    
#a=[1,4,5]
#b=[2,3,3]
#c=[1,2,3]
#result=triplets(a,b,c)
#print(result)

#------5. Minimum Time Required-----------#
# Amazing Approach
# 1. Binary Search for the Day
# 1. A very differnt way of applying binary search
# 2. The longer approach is that you check for everyday that how many machines
# can deliever on that day

#def numberOfItems(dayNumber,machines):
#    countOfItems=0
#    tempItems=0
#    for number in machines:
#        tempItems=dayNumber//number
#        countOfItems+=tempItems
#    return countOfItems
#    
#def binarySearch(machines,left,right,goal):
#    bestDayNumber=0
#    while(left<=right):
#        dayNumber=left+(right-left)//2
#        itemCount=numberOfItems(dayNumber,machines)
#        if(itemCount>=goal):
#            bestDayNumber=dayNumber
#            right=dayNumber-1 
#        else:
#            left=dayNumber+1
#
#    return bestDayNumber
#    
#def minTime(machines, goal):
#    left=min(machines)
#    right=goal*max(machines)
#    numberOfDays=binarySearch(machines,left,right,goal)
#    return numberOfDays
#
#machines=[4,5,6]
#goal=12
#result=minTime(machines, goal)
#print(result)













