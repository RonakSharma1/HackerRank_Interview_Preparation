#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:25:31 2020

@author: ronaksharma
"""
#-------------- STRING MANIPLULATION-----------------#
# 1. Fomatting Strings
# x="hellp {0} my name {1} knsdf {2}"
# x.format(2.0,1,"cael"); these are placeholders, the type
# However the number of entries matter
# can take any type and can be less or more thatn teh {} existeing in the string
# OR
# s= 'In %d years I have spotted %g %s.' then,
# s%(3, 0.1, 'camels') i.e. s modulus tuple will replace those elements
# The number and type of elements shoudl match here

#--------- Exercises----------#


# 1. For reversing a string, use Stacks
#Alternating Characters#
#def alternatingCharacters(s):
#    s=list(s)
#    counter=0
#    for i in range(len(s)-1):
#        if(s[i]==s[i+1]):
#            counter+=1
#    return counter
     
#result=alternatingCharacters("BABABA")
#print(result)

# 2. Replacing a characters belonging to a list from another list
# METHOD1: Use import re, then re.sub('a|e|r',' reaplce with', test_String)

#Making Anagrams#
# 1. Strings are immutable i.e there is size cannot be changed. Hence cannot add or subtract elements
# 2. Convert Strings to list. Becomes Mutable
#
#def makeAnagram(a, b):
#    a_set=set(a)
#    b_set=set(b)
#    counter=0
#    intersection=a_set&b_set
#    set_diff=(a_set|b_set)-(a_set&b_set)
##    print(set_diff)
#    if(len(set_diff)==0):
#        counter=0
#    else: 
#        for i in set_diff:
#            temp=max((a.count(i),b.count(i)))
#            counter=counter+temp
#    intersection=list(intersection)
##    print(intersection)
#    if(len(intersection)!=0):
#        for i in intersection:
#            if(a.count(i)!=b.count(i)):
#                diff=abs(a.count(i)-b.count(i))
#                counter=counter+diff
#    return counter
#
#a="fcrxzwscanmligyxyvym"
#b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"
#result=makeAnagram(a,b)
#print(result)r



#-------- String Interleaving---------#
# Two strings are shuffled to form a third string such that the order is maintained
#def interLeaving(s1,s2,s3):
#    if(len(s1)+len(s2)!=len(s3)):
#        return False
#    m=n=0
#    x=True
#    for i in range(len(s3)):
#        if(m==len(s1)):
#            m=0
#        elif(n==len(s2)):
#            n=0
#            
#        if(s3[i]!=s1[m] and s3[i]!=s2[n]):
#            x=False
#            break
#        elif(s3[i]==s2[n]):
#            x=True
#            n+=1
#        elif(s3[i]==s1[m]):
#            x=True
#            m+=1
#    return x 
#s1="aabc"
#s2="def"
#s3="daeabcf"        
#result=interLeaving(s1,s2,s3)
#print(result)            



# --------FIRST NON REPEATING STRING-----------#
# 1. Use dict to store the occurence and then loop again throguh the string
# to see and break at character which has a occcurnce of 1
# 2. sort the array and compare for i-1 and i+1 and break



#------------Sherlock and the Valid String------------#
## 1. Logic: Create a Counter for frequency of characters. Then create another 
## Counter to track the how many elements are repeated the same number of times
## Once done, create a list of that and check the number of elements in that.
## 2. Condition 1: Elements list of list can only contain 2 elements. So check
## differnce of occurence is 1 and if either one has an occurence of 1, then YES
## The other OR checks if any element is just present once, so remove it

#from collections import Counter
#def isValid(s):
#    s=Counter(s)
#    freqCount=Counter(s.values()) # or len(set(s.values()))
#    if(len(freqCount)>2):
#        return "NO"
#    elif(len(freqCount)==1):
#        return "YES"
#    else:
#        elements=sorted(freqCount.items())
#        differenceOfValues=elements[1][0]-elements[0][0]
#        # Condition 1
#        if(differenceOfValues==1 and (elements[0][1]==1 or elements[1][1]==1) or((1,1) in elements)):
#            return "YES"
#        else:
#            return "NO"
#s="aaaabbbbc"
#result=isValid(s)
#print(result)

#----------Special String Again-----------#
# ** A single pair combinations is n(n-1)/2 and for a pair of 2 or 3 is count(pair1)*count(pair2)
# 1. Initilaise count here to n as that will be minimum value
# 2. in an If condition the first condition will be checked an d if false the rest will not
# be executed. This allows to check i+j and then perform s[i+j]
# 3. Consider all perimutations i.e. 1+2+3+4
#def substrCount(n, s):
#    count=n
#    start=0
#    prev=None
#    for i,c in enumerate(s):
#        if(i==0):
#            prev=c
#        elif(c==prev):
#            count=count + (i-start) # i- start ensures 4+3+2+1 so all possible combinatons
#        else:
#            for j in range(1,i-start+1):
#                #(i-j)>=0 to check if the middle element is at s[1], then we don't go beyond the s[0]
#                # From midlle element start moving forward and backward              
#                if((i-j)>=0 and (i+j<len(s)) and s[i-j]==s[i+j] ):
#                    count+=1
#                else:
#                    break
#            prev=c
#            start=i
#    return count
#n=5
#s="asasd"
#result=substrCount(n,s)
#print(result)




#---- Run Length Encoding Problem-----#
# 1. Clean Code, Heuristic Approach, Fundamentals
# 2. Don't jump into problem, talk about loud, disambiguate ask questions like edge cases and I/O
# 2a. Ask for order of the input, ask if any alphanumeric string
# 3. Check if the input is valid like s!=None or number!=0
# 4. Write full variable names
# 5. Write a comment when staring a new functionality
# 6. Test your code with an input and show that it works
# 7. Think about cases that might break or how to optimise if you can. But do at least brute force
#def runLengthEncoding(s):
#    counter=1
#    encoding=[]
#    n=len(s)
#    for i,word in enumerate(s):
#        if(i==n-1):
#            if(s[i]==s[i-1]):
#                encoding.append([s[i],counter])
#                break
#            else:
#                encoding.append([s[i],1])
#                
#        elif(s[i]==s[i+1]):
#            counter+=1
#        else:
#            encoding.append([s[i],counter])
#            counter=1
#
#    return encoding

#def runLengthEncoding(s):
#    prevChar='0'
#    counter=1
#    encoding=[]
#    for currentChar in s:
#        if(currentChar==prevChar):#prevChar is fixed at the first interval if same
#            counter+=1
#        else:
#            if(prevChar!='0'):
#                encoding.append([prevChar,counter])
#            counter=1
#            prevChar=currentChar
#    encoding.append([prevChar,counter])
#    return encoding

#imageFile="aabcc"
#outcome=runLengthEncoding(imageFile)
#print(outcome)

#---5.--------Common Child-----------#
#---------DID NOT UNDERSTAND THIS------#
#def commonChild(s1, s2):
#    m = len(s1) 
#    n = len(s2) 
#    listOftheNumber = [[None]*(n+1) for i in range(m+1)] 
#    for i  in range(m+1):
#        for j in range(n+1):
#            if(i==0 or j==0):
#                listOftheNumber[i][j]=0
#            elif(s1[i-1]==s2[j-1]):
#                listOftheNumber[i][j]=listOftheNumber[i-1][j-1]+1
#            else:
#                listOftheNumber[i][j]=max(listOftheNumber[i-1][j],listOftheNumber[i][j-1])
#
#            
#    return listOftheNumber[m][n]
#
#s1="HARRY"
#s2="SALLY"
#outcome=commonChild(s1,s2)
#print(outcome)


                                                                           