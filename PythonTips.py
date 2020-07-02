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
# Website: https://realpython.com/regex-python/


# 1. For complex string matching or pattern matching in strins
import re
s1="foo123bar"
s2="foo247"
s3="foo13bar"

# Character Class
# 1. Set of characters specified in square brackets i.e. ('[][][]') makes a CHARACTER CLASS
# 2. Leftmost possible search result is returned
# 3. '^': COMPLEMENTS  a Character Class
# 4. Use backslash '\' to find special characters or put them in start or end of []
# 5. Most special characters like '*','+'loose their meaning inside [] i.e. [)*+] finds these characters
# 6. \d and \D: Similar to [0-9], \s and \S: Looks for whitespaces
# 7. \A and \Z: Checks if string present at front and end respec. Ex '\Afoo' for front and '\Zbar' for end
# 8. '\bxxx': Check if the word you are searching is the beginning or end of another word. So 'foo bar' but  'foobar' one word
# 9. '*','+' and '?' are greedy (Longest Possible Match)
# 10. '??','.*?' etc are non greedy(Shortest possible match) [Example later]
print(re.search('[0-9][0-9][0-9]',s1)) #Inclusive of 0 and 9 character class
print(re.search('fo[ourt]',s1))# Checks if the next character after 'o' belongs to these set of characters
print(re.search('[^0-9]', '12345foo')) # ^ searches for first character i.e. not a string
print(re.search('[\^#:]', 'foo^bar:baz#qux')) # Finds '^'
print(re.search('[-abc]', '123-456')) # finds '-' or use [abc-] or [a\-c], means a,c and -               

# Dot expression
# 1. Returns True if there exists a character b/w the start and end character
# 2. Each '.' is a placeholder, so multiple dots required if looking for more than two words
print(re.search('1.3',s3)) # False: It checks if there is a '1', then any character and finally a '3'
print(re.search('o.2',s1)) # True
print(re.search('foo.bar', 'fooxbar')) # True
print(re.search('foo.bar', 'foo12bar')) # False
print(re.search('foo..bar', 'fooxbar')) # True: Due to two '.' experessions

# \w and \W Expression
# 1. \w: Alphanueric Search similar to  doing : [a-zA-Z0-9_]
# 2. \W: Complement of the above
re.search('\w', '#(.a$@&') # 'a' is the first match
re.search('\W', 'a_1*3Qb') # Complement is used. So '*' is the first match

# '*': The preceding character is repeated zero or infinite number of times
# '+': The preceding character is repeated at least once
# '?': The preceding character occurs only once or not at all
# 1. Ex 'ca*t' means that 'ct','cat','caaaat' all are acceptable
re.search('foo.*bar', '# foo $qux@grault % bar #') # Matches anything b/w foo and bar as '.' here represents multiple placeholder due to '*'
re.match('foo[1-9]*bar', 'foo42bar') # Using metaclass and '*' together

# Greedy Search Operations
re.search('<.*>', '%<foo> <bar> <baz>%') # Spans 1 to 18. Result= ['<foo>....>']

# Non Greedy
re.search('<.*?>', '%<foo> <bar> <baz>%') # Spans 1 to 6. Result=['<','f','o'..'>']
# OR use ' <[^>]*>'

# Quantifying the Repitions
# 1. {m}: Matches m repitions of predecing regex
# 2. {m,n}: Matches m upto n repitions. Ex -{2,5}, so everything from 2 dashes to 5 are accepted
# 3. {m,}: Any repitions greater than m
# 4.  {,n}: Any repitions upto n. Also {}!={,}
re.search('x-{3}x', 'x---x') # {m} expression
re.search('x-{2,4}x', 'x--x') # AND 'x---x' are both acceptable strings
re.search('a{3,5}', 'aaaaaaaa') # Greedy. Returns 'aaaaa..'. Max possible length
re.search('a{3,5}?', 'aaaaaaaa') # Non Greedy as returns just 'aaa'

# Grouping and Paranthesis
# 1. Create complicated regex for patern matching. Ex '(foo(bar)?)+(\d\d\d)?'
# 2. (bar)+ VS bar+ : Checks for repitions of 'bar' instead of 'r..'
# 3. (ba[rz]){2,4}: 2 to 4 repitions of bar or baz

      
# Capturing Groups
m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
m.groups() # Returns ('foo', 'quux', 'baz'). Also can do groups(1,2,3)
m.group() # Same as m.groupS(0)

# Backreference: Matches content of previously captured group
# 1. '([a-z])#\1': If this is used instead of raw string, Python interprets it as hexadecimal
regex = r'(\w+),\1'
m = re.search(regex, 'foo,qux') # False as qux!=foo
m = re.search(regex, 'foo,foo') # True as foo is captured and then it looks for foo again

# Conditional Match
regex = r'^(###)?foo(?(1)bar|baz)' # Mathces ###, then if group 1 exists it checks for 'bar' otherwise for 'baz'
# Since this is a raw string so '^' here means the start and not the complement

# Pipe Function: Non greedy so will search from left to right and exit as soon as a match is found
re.search('foo|grault', 'foograult') # Returns true of matches any of the alternatives
re.search('(foo|bar|baz)+', 'barbazfoo') # Matches the regex as well