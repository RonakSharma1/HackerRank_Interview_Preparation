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


#----------- Built in Functions--------#
# 1. abs(): returns positive number. in case of a complex number, returns the magnitude 
# 2. ascii(): Replaces any non-ascii characters with escape characters
# 3. all() and any(): Checks if values in an iterable are True or False. No conditional statements
# 4. bool(): Returns false when condition is false or an empty object is passed. Otherwise True
# 5. bin(): Converts integer to binary
# 6. bytes(): Integers not much change but Strings are converted to Bytes
# 7. chr(): Converts ASCII to character. Only integer as argument
# 8. ord(): Converts character to ACSCII (Not Strings)
# 9. complex(): Creates imaginary number.Ex- complex(1,2) and complex("1+2j") outputs 1+2j
# 10. divmod(a,b): Returns the quotient and remainder pair. Works differently for both integers and floats
# 11. enumerate(): Input must bue an Iteratable. Returns a list of tuple i.e. (position,value) = [(0,'asd'),(1,'gdf'),....]
# 12. eval('string'): Input is a string like a mathematical expression and calculates the answer for a particular value. Ex- x=4, eval('x+2+(x*2)')
# 13. filter(function,list) or filter(lambda func): Filters a list. 
#  Ex- filter(lambda x: x % 2 != 0, [1,2,3,4]), outputs= [1,3]
#  The elements are only added if they return True from the function. Map will not do that
# 14. float(string)and map(): Float Strings to floats values
# 15. frozenset(list): Immutable version of set that cannot be modified
# 16. hash(): Return an integer value i.e. a hash. Input is usually strings or floats. For Integers the hash is same as the value
# 17. hex(): Converts integers to hexadecimal
# 18. id(): Assings a unique identitiy to objects based on their values. x=4 and y=4 have same identity
# 19. iter(): Converts lists to iterator so can only traverse once in run time. Uses 'next' to move to the next element
# 20. open(): Opens a file of a type. Default mode is 'read'
# 21. pow(base,exp,mod=x): Returns base**exp i.e. (10**2). Or (10**2 mod x)
# 22. round(float): round(0.5)=0 and round(1.5)=2 because rounding is done to even integers in case the argument is equally close to both upper and lower boudn

#--------------------------- Itertools------------------------#
# 1. Functions here operate on "iterators" to produce more complex iterators. Using
# iterator algebra is useful as it leads to better memory efficiency and faster execution time
# Tutorial: https://realpython.com/python-itertools/
# 2. map(len,[1,2,3]) and zip(x,y) are example of itertools
# 3. To use this library, ensure that the data type is 'iter'. Example iter(list(x))
# 4. Similarly, LISTS of TYPE ITER, cannot undergo 'Slicing' or 'Appending'

import itertools as it

# ----------Combinations and Permutations---------------#
# 1. Comb: A choice of k things from a set of n things
# 2. Perm:All possible rearragements of elements in a list. Calculated using n!
list(it.combinations([1,2,3], 2)) # Return successive n-length combinations of elements in the iterable without repeating individual elements
list(it.combinations_with_replacement([1,2,2,4], 2)) #Return successive n-length combinations and allows individual elements to have successive repeats.
# The above will only extra elemetns like (1,1),(2,2,) and (3,3)
# set(exampleOutout) # To remove repeated elements/tuples use 'SET'. 

list(it.permutations('abc'))# Argument can  be a list of elements


# ----------Sequences of Numbers---------------#
# 1. Produce infinite sequence of numbers using generators
# 2. Infinite series are useful when using ZIP as shown in example

example = it.count(start=1, step=2) # OR (start=1, step=0.75) OR (start= -1, step= -2)
list(next(example) for _ in range(5)) # Use next here as it is a generator

# Iterated through a list without knowing its length
list(zip(it.count(), ['a', 'b', 'c']))

# ----------Recurrence Relations---------------#
# Use 'next()' to iteratre through this as it is a generator
repeat=it.repeat(1,5) # Repeats 1 five times i.e. 1 1 1 1 1
cycle = it.cycle([1,2,3]) # Repeats this cycle infinitely, 1 2 3 1 2 3 ...

# Recursion
list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: x - y)) # x is the previously updated element and y is the current element

#----- Dealing a Deck of Cards----------#

# Cartesian Product: Equivalent to nested for-loops.
it.product([1, 2, 3], ['a', 'b'], ['c']) # Returns a cartesian produc of all combinations. This case tuples of 3 elements

# Teeing
iterator1, iterator2 = it.tee([1, 2, 3, 4, 5], 2) # Creates 2 copies of this, which will get exhausted once called
list(iterator1)
list(iterator1)  # iterator1 is now exhausted.
list(iterator2)  # iterator2 works independently of iterator1

#Slicing
# This increases space complexity as you make a copy of the original list and return a new list with the selected elements.
list(it.islice([1, 2, 3, 4, 5], 0, 5, 2)) # Slice till 5 in steps of 2

# Chaining
list(it.chain([1, 2], [3, 4, 5, 6], [7, 8, 9])) # Gives [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filtering
only_positives = it.filterfalse(lambda x: x <= 0, [0, 1, -1, 2, -2]) # [1,2]
it.takewhile(lambda x: x < 3, [0, 1, 2, 3, 4])  # 0, 1, 2
it.dropwhile(lambda x: x < 3, [0, 1, 2, 3, 4])  # 3, 4

# Compressing
it.compress('ABCDEFG',[1,0,0,1]) # Returns 'A' and 'D'. Removes the rest of the elements
it.compress([12,23,54,767,123,43,54],[1,0,0,1]) # Returns [12,767]