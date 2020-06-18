#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:23:35 2020

@author: ronaksharma
"""
#-------------- DICTIONARIES AND HASHMAPS-----------------#
# 1. Useful for looking up or finding any values
# 1. Key Value where KEYS are unique
# 2. A hash table is used to fetch, add and remove an element in constant time
# 2. Strings mapped to Hashcodes mapped to Index
# 3. Dictionaries can store 1:'Alex' or 1:[1,2,3,4] a list even!!
# 3. Possible to have two diferent strings "aLEX" and "Bob" mapped to same array index i.e a[0]
#   In such case collion and so you store a[0]= list of list {"p1","Alex", "p2"..}
# 3. Runs in O(1) times, worst case is O(n)
# 4. BE GREEDY. Try to optmise or gain the most out of in one singel loop rather
# than dividing the code
# 5. If key does not exits, then defaultdict(list) returns [] empty list. Example
# d['a'].append(1): This will automatically add 'a' in dict and append '1' to it without any error
# 6. Searchign in dictionary takes O(1) as it si a hashtable. So i in dict(), takes O(1) time
# 7. Keys are not mutable in a dict. So You can never use LISTS as keys because they are mutable
# However you can use tuples as keys because they are immutable
# So mutable datatypes are not hashable but immutable types like strings and integers are hashable
# 8. Dict features 'setdefault' and 'get' to deal with inexisting values
# setdefault('name','not exists') OR x= d.get('name','does not exists') ; if exists print the value otherise the default
# 9. Conver d.items() to a list to access elements. 
# So loop using this if required to acces both key and value at the same time
# 10. Common to use tuples as keys as tuples are like key,value pairs only
# 11. Sorted(dictionary): sorts by key values by default in ascending order
# 12. set(d) is a set of Keys of a dictionary
# 13. set(a) <= set(b) checks if set a is a subset of set b
    
#-----Example of creating a Dictionary using Tuple------
# In below cases ensure that keys are not repeated so 'a' and then 'a' not repeated
#t = [('a', 0), ('c', 2), ('b', 1)]
#d = dict(t)
#print(d)
#OR
#d = dict(zip('abc', range(3)))
#-----------------------------------------------#

#Ransom Note#
# 1. Using the below code fails to execute within time due to For Loop and count
#def checkMagazine(magazine, note):
#    for i in note:
#        if(note.count(i)!=magazine.count(i)):
#            return "No"
#    return "Yes"

#def checkMagazine(magazine, note):
#    x=0
#    mag=dict()
#    for i in magazine:
#        if(i in mag):
#            mag[i]+=1
#        else:
#            mag[i]=1
#    for i in note:
#        if(i not in mag):
#            x=1
#            break
#        else:
#            mag[i]-=1
#            if(mag[i]==-1): # Signifies that not equal number
#                x=1
#                break
#    if(x==1):
#        print("No")
#    else:
#        print("Yes")
#    
#magazine=['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts','some','some']
#note=['ive', 'got', 'some', 'coconuts','some']
#result=checkMagazine(magazine,note)

#Two Strings#
# Very Easy

# Sherlocks and Anagrams#
# 1. Use A[ASCI Value]="String". This way all those string having the same sum can be found
# which will essentially be the duplicates
#def sherlockAndAnagrams(s):
#    subStrings=dict()
#    counter=0
#    n=len(s)
#    for i in range(n):
#        for j in range(i,n):
#            add=sorted(s[i:j+1])
#            add=''.join(add)
#            if(add in subStrings): # Need to look-up the element, hecne why Hashmap
#                counter=counter+subStrings[add]
#                print(counter,add)
#                subStrings[add]+=1
#            else:
#                subStrings[add]=1
#            
#    return counter
#    
#s="cdcd"
#result=sherlockAndAnagrams(s)
#print(result)

#------------ Frequency Queries----------#
#
#def freqQuery(queries):
#    d=dict()
#    for i in range(len(queries)):
#        if(queries[i][0]==1):
#            if(queries[i][1] not in d):
#                d[queries[i][1]]=1
#            else:
#                d[queries[i][1]]+=1
#        elif(queries[i][0]==2):
#            if(queries[i][1] in d.keys()):
#                d[queries[i][1]]-=1
#            else:
#                None
#        elif(queries[i][0]==3):
#            if(queries[i][1] in d.values()):
#                print(1)
#            else:
#                print(0)
#        else:
#            None
#    
#    
##queries=[[3, 4], [2, 1003], [1, 16], [3, 1]]
##queries=[[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]
##queries=[[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
#queries=[[1,4],[1,3],[2,3],[2,4],[2,10],[2,20],[3,1],[2,5],[3,1]]
#freqQuery(queries)

#----------------Count Triplets--------------#
# 1. Counter returns 0 if a key does not exists
# 2. Inputting an array in Counter automatically calculates the frequency
# 3. Counter.most_common(2) given the 2 most common keys. If no arguments, returns
# the key is descending order of the frequency
#from collections import Counter
#
#def countTriplets(arr, r):
#    first_element=Counter()
#    third_element=Counter(arr)
#    count=0
#    for mid in arr:
#        third_element[mid]-=1 # If not done, repeated elements will count 4 times intead of 2 like 4,4
#        count_1=first_element[mid/r]
#        count_2=third_element[mid*r]
#        first_element[mid]+=1
#        count=count+(count_1*count_2)
#    return count
#        
#arr=[1,5,5,25,125]
#r=5
#result=countTriplets(arr,r)
#print(result)

























