#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:39:22 2020

@author: ronaksharma
"""
# 1. Using modulus you can calculate the first or last two digits of a number by
# just taking modulus with %10 and %100
# 2. Use While loops when you need to change the position in search when a condition
# is satisfied. A For loop would not allow to change the 'i' th index without breaking
# 3. Every mutable structure like LISTS are passed by reference, somewhat like global variable
# 4. Object and Value are two different things. a=[1,2,3] and b=[1,2,3]
# Every object has a value. An association of a varaible with an object is called referece. So if
# a and b are list and a=b, so we say that there are two references to the same object
# 5. Alisaing: When a single object has more than 1 reference. Problem with lists but not with 
# 6. When you pass a list to a function it gets the reference to the list and not the list itself (EXAMPLE BELOW)
# So a is b = False as they have te same value, but they are diiferent objects. These 
# lists are equivalent but not identitical. This problem is not with  Strings
# As strings create one string object and both 'a' and 'b' refer to it
# 7. Searchign in list takes O(n) as it needs to go through each elements. So i in list(), takes O(n) time
# 8. d=dict(), now d.get('uno',0): It check if 'uno' exists in d and if not it returns a default value of 0. 
# Using this helps remove the if conditional statements
# 9. Reverse lookups i.e. given value find key are costly and not O(1)
#10. To add multiple elements t=t+[2]*n
# 11. Use lists to compare multiple variables simultaneouly [x,y,z]>[a,b,c]
#------------- Reference to the List Example------------#

#---- Example 1 *****
"""
At the beginning of bad_delete_head, t and t4 refer to the same list. At the end, t refers
to a new list, but t4 still refers to the original, unmodified list.
"""
#def bad_delete_head(t):
#    t = t[1:] # Creating a new list here so reference would not matter
#    del t[1:] # Now will affect origninal list as modifying
#t4 = [1, 2, 3]
#bad_delete_head(t4)
#print(t4) 

# Most LIST methods return None so doing this t = t.sort(), would fail and would
# initialise t to None as the sort method would have retunrned None
# This is however not a problem with immutbale objects like Strings ex. word=word.strip()
# To combine two lists use t+x or t.extend(x)

#-------- Example 2 ****
#x=[1,2,3]
#y=x # Now both x and y refer to the same object, So changes in either of these will be reflective in both the lists
#z=x[:]
#x[0]=10
#print(x,y,z)

#--------------------------------------------------------#

#-------------------TUPLES------------#
# 1. t = tuple('lupins')
# 2. Slicing is possibe in tuples
# 3.(0, 1, 2) < (0, 3, 4) {Checks element vise for each index}
# 4. Combine tuples like lists
# 5. a,b=b,a is essentially a tuple and so a,b,c=b,a,c is also valid
# Similarly, a,b,c=x.split(','). If you are sure only 3 elements will be returned then use tuples
# 6. return max(t),min(t) essentially return tuples. So returnin tuple is like
# returning multiple values
#------- Example 1
#For passing a sequence of values and want to pass to a  
# function as multiple arguments use the * operator

# --- Scattering Example--#
#t=(1,2)
#divmod(*t) #Inputing a tuple as '*' scatters the tuple

#---Gathering Example---#
#def sum_all(*args): # Declaring a * argument gathers all inputs into a singel tuple
#    summation=sum(args)
#    print(summation)
    
# 7. Zip: Connects two or more lists thus creating a LISTS OF LIST
# 1. Indexing possble through lists
# 2. Multiple inputs zip(x,y,z,v..)
# 3. Different sizes. Will only zip until the size is same. The rest elements will be ignored
# 4. Traverse list using tuple argument for (x,y) in..
#x="abc"
#y=[1,2,3]
#a=[4,5,6] # zip(x,y,a) Multiple arguments possible
#z=zip(x,y)
#z=list(z)
#print(z,z[0]) #This way you can access index

# Traversing a list
#def has_match(t1, t2):# Checks the if same elements at an index
#    for x, y in zip(t1, t2):
#        if x == y:
#            return True
#    return False

#-------------



#-------------------------------------#



# ---------------ARRAY----------------#
# 1. Check for if sorted, negative values, duplicates, index
## 2D ARRAY DS #
## 1: USE NESTED LOOPS WITH 2D ARRAY
## 2:Either use the first value of array to initiliase or use a value that is not in constraints
#
#def hourglassSum(arr):
#    numberOfTraverse=4
#    i=0
#    j=0
#    hourglass=[]
#    maximumValue=-100
#    while(i<numberOfTraverse and j<numberOfTraverse):
#        topRow=arr[i][j:j+3]
#        midRow=arr[i+1][j+1]
#        botRow=arr[i+2][j:j+3]
#        hourglass=topRow+[midRow]+botRow
##        print(hourglass)
#        temp=sum(hourglass)
##        if(i==0 and j==0):
##            maximumValue=temp
#        j=j+1
#        if(j==4 and i!=3):
#            i=i+1
#            j=0
#        if(maximumValue<temp):
#            maximumValue=temp
#        
#    return maximumValue
#
#arr1=[[-1,-1, -1, 0, -10, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]    
#arr2=[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]
#arr3=[[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
#arr4=[[-1,-1, -1, -1, -1-1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]
#result=hourglassSum(arr2)
#print(result)

# MINIMUM SWAPS 2
# 1. WHEN NOT EXECUTABLE DO NOT YOU SEARCH
# 2. When elements are not missing then you can you the actual value of the element as its location
#def minimumSwaps(arr):
#    swaps=0
#    i=0
#    while(i<len(arr)): # Until you have reached the end of the array
#        if(arr[i]!=i+1):
#            x=arr[i]-1
#            arr[i],arr[x]=arr[x],arr[i]
#            swaps=swaps+1
#        else:
#            i=i+1
#    return swaps
#
#arr=[1,3,5,2,4,6,7]
#result=minimumSwaps(arr)
#print(result)

# ARRAYS LEFT ROTATION

#def rotLeft(a, d):
#    for i in range(d):
#        temp=a.pop(0)
#        a.append(temp)
#    return a
#    
#arr=[1,2,3,4,5]
#d=4
#result=rotLeft(arr,d)
#print(result)

#-------4------New Year Chaos-----------#
# 1. Think about what to count: Here number of people who were bribed instead of the bribers
# 2. range(max(0,q[pos])): Useful way to use range and take care of first and second index
# 3. Count from the orginial postiiton of the member till its current position
# Count the numbers greater than itself and thats the total number of times it was bribed
# Motivation: The briber can be either in the next position of two positions ahead, so start counting
# from that point until its current position because it could have been bribed by mutiple briber
# No need to check after it as that means those values have not bribed out current value
#def minimumBribes(q):
#    countOfBribes=0
#    bribeIsInvalid=0
#    totalNumberOfBribes=0
#    for pos in range(len(q)):
#        if(q[pos]-1-pos>2):
#            bribeIsInvalid=1
#            break
##        print(q[pos],q[pos]-1,pos+1)
#        for i in range(max(0,q[pos]-2),pos+1):
#            if(q[i]>q[pos]):
#                countOfBribes+=1
##        print(q[pos],countOfBribes)
#        totalNumberOfBribes=totalNumberOfBribes+countOfBribes
#        countOfBribes=0
#    if(bribeIsInvalid==1):
#        print("Too chaotic")
#    else:
#        print(totalNumberOfBribes)
#
#arr=[1,2,5,3,7,8,6,4]
#arr=[2,1,5,3,4]
#arr=[2,5,1,3,4]
#minimumBribes(arr)
       
# TIME FAILURE: Counting the number of people who have bribed
#    countOfBribes=0
#    bribeIsInvalid=0
#    for pos in range(len(q)):
#        if(q[pos]-1-pos>2):
#            bribeIsInvalid=1
#            break
#        for currentPos in range(pos+1,len(q)):
#            if(q[pos]>q[currentPos]):
#                countOfBribes+=1
#
#    if(bribeIsInvalid==1):
#        print("Too chaotic")
#    else:
#        print(countOfBribes)
             
#q=[2,1,5,3,4]
#minimumBribes(q)


#--------- Find a missing Number-------#
# If continous array, calculate the sum of natural number untiol n and then
# subtract the sum of the given array to find the missing number
#--------------OR-----------------#
# result=0
# for i in arr_old+arr_new:
#   result=resul^i (XOR with same number twice has no affect. So at the end missing
# number will be left in the result)

#------ Finding first and second smallest element   ------------# 
# 1. Maintinating two pointter
#https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/
#def firstAndSecond(arr):
#    first=second=arr[0]
#    for i in range(1,len(arr)):
#        if(arr[i]<first):
#            second=first
#            first=arr[i]
#        if(arr[i]<second and arr[i]!=first):
#            second=arr[i]
#    return first,second
#arr=[12,25,8,55,10,33,17,11]
#one,two=firstAndSecond(arr)
#print(one,two)


#------Look at Kadane's algorithm------#
# Maximum subarray probelem
#def largestContinousSum(arr):
#    currentSum=currentMax=arr[0]
#    for i in range(1,len(arr)):
#        currentSum=max(arr[i],arr[i]+currentSum)
#        currentMax=max(currentSum,currentMax) #important as for -2 and -2-1 the number will become -2 if this conditio not there
#    return currentMax
#  
#
#arr=[-2, -3, 4, -1, -2, 1, 5, -3]
#result=largestContinousSum(arr)
#print(result)

#-----------XOR Concept-------#
#1. XOR same element even times produces 0 and odd times create 1
# 2^2=0 and 2^2^2=2 not 1


#------Find Next Palindrome Number---------#
# 1. Given 125, answer is 131
# 2. For odd numbers mirror along the centre and add 1 to the mid if smaller
# 3. For even mirror along centre and if smaller add 1 to both mid and mid+1 element


#--------Find Next Higher Number With Same Digits-------#
# 1. Given 1234 anwer is 1243, 12543 gives 13245
# Algorithm: Starting from end, compare the two elements and if smaller. Sort the array
# and then replace with the smallest values. Then arrange evrythning in sorted fashion

#------ Sum of Subarray equal to a value K---------#







