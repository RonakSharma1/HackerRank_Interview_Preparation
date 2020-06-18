#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:47:52 2020

@author: ronaksharma
"""

#------------- BINARY SEARCH TREES-------------#

# 1. Each BST has one root node and each node has only max of two nodes
# 2. Three traversal operation, inorder, preporder postorder
# 3.Leaf is the end node

# Example 1: Inserting a Node in BST
#class Node:
#    def __init__(self,data):
#        self.data=data
#        self.right=None
#        self.left=None
#    
#    def add(self,node):
#        if(self.data<node):
#            if(self.right==None):
#                self.right=Node(node)
#            else:
#                self.right.add(node)
#        else:
#            if(self.left==None):
#                self.left=Node(node)
#            else:
#                self.left.add(node)
#        
#    def contains(self,value):
#        if(value==self.data):
#            print("Yes")
#            return True
#        else:
##            print(self.data)
#            if(self.right==None and self.left==None):
#                print("No")
#                return False
#            elif(value<self.data):
#                self.left.contains(value)
#            else:
#                self.right.contains(value)
# 
#    def pathPrint(self,value):
#        if(value==self.data):
#            print(value)
#        else:
##            print(self.data)
#            if(self.right==None and self.left==None):
#                return False
#            elif(value<self.data):
#                self.left.pathPrint(value)
#            else:
#                self.right.pathPrint(value)
#
#root=Node(6)
#root.add(2)
#root.add(5)
#root.add(1)
#root.add(7)
#root.pathPrint(7)


# ----Height of Binary Tree----#
# 1. Only Immutable are passed by Reference. So Lists can be passsed and when changed in 
# another function, they can be printed as it is. However a variable can be changed in a funciton
# but will maintian the initilisation value
# -------- O(n) Time Complexity --------#
# 2. Passing variables in recurssion matatins different values at different levels
# 3. The Pre, Post and Inorder Traversal differ in that where does the logic goes
# that does something with the root.info. So should it before traversing, middle or after

#def traverse(root, depth):
#    if root==None:
#        return depth-1
#    else:
#        depthOfLeft = traverse(root.left, depth+1)
#        depthOfRight = traverse(root.right, depth+1)
#        return max(depthOfLeft, depthOfRight)
#    
#def height(root):
#    depth=0
#    heightOfTree = traverse(root, depth)
#    return heightOfTree
    
#--- Lowest Common Ancestor---#
#def traverse(root,v1,v2,node):
#    if root==None:
#        return None
#    elif root.info==v1:
#        return root
#    elif root.info==v2:
#        return root
#    else:
#        v1NodeFound=traverse(root.left,v1,v2,node)
#        v2NodeFound=traverse(root.right,v1,v2,node)
#        if(v1NodeFound!=None and v2NodeFound!=None):
#            if((v1NodeFound.info==v1 or v2NodeFound.info==v1) and(v1NodeFound.info==v2 or v2NodeFound.info==v2)):
#                # print(root,v1NodeFound,v2NodeFound)
#                return root
#        if(v1NodeFound.info!=0):
#            return v1NodeFound
#        elif(v2NodeFound.info!=0):
#            return v2NodeFound
#        else:
#            return None 
#def lca(root, v1, v2):
#    node=[]
#    output=traverse(root, v1, v2,node)
#    return output 

#-------- Huffman Decoding------#
#------------ DONE-------------#

#-------- Is this a Binary Tree-------#
# 1. InOrder ensures that BST is printed in order
# 2. Never use variables in InOrder as it might have different values as it
# lies between the left and right traversal
#-------------Done--------------------#



#-------Level Order Traversal-------#
#class Node:
#    
#    def __init__(self,data):
#        self.data=data
#        self.left=None
#        self.right=None
#    
#        
#        
#def levelOrderTraversal(node):
#    queue=[node]
#    while queue:
#        currentNode=queue.pop(0) 
#        print(currentNode.data,end=' ')
#        
#        if(currentNode.left!=None):
#            queue.append(currentNode.left)
#            
#        if(currentNode.right!=None):
#            queue.append(currentNode.right)
#                
#    
#root = Node(1) 
#root.left = Node(2) 
#root.right = Node(3) 
#root.left.left = Node(4) 
#root.left.right = Node(5) 
#levelOrderTraversal(root)     


#-------- Converting BT to BST--------#
# 1. In order to get the curent stauts and then sort it to get the actualt BST
# 2.Then traverse the treee until reached left and replace the data with the value
# from the first element. Then arr.pop(0) remove it. This
# 3. Rather than adding edges again from scratch, just replace the data**



#-------Counting vertical sum of a tree------#
# 0,+1,-1 and increment and decrememtn depending on turn\
# Use inorder traversal
#-------Maximum Width------#
#Do level order traversal and find the maximum number of nodes in a queue at any given time of the loopoing


#-------Minimum distance from root to node or a leaf--------#
# Just using a level order traversal
# if x.left and x.right == None return depth



#---------MIN HEAP---------#
# 1. A tree where the minimum value is at the root and traversing down, for each
# node, its child are always bigger than itslef
# 2. Use array to store the left and right child by using Index i.e.
# prnt=(index-1)//2 , lftChild=index*2 + 1 rightChild=index*2 + 2 
# 3. When removing the smallest elemetn i.e. root. Replace the root by the last
#  added element in the array and then reduce the aray size. After that you need to
# heapify down i.e. compare the root to the left and right child and swap with the 
# smallest of both, Repeat this until reached the rquired positions
# 4. To add a new node, you add it to the end of the array and then heapify it up
# this means that, comparing the parent and the child and swapping if the child is 
# smaller. This way automatically find its way in the heap


#---------------TRIE------------#
# 1. Used for word validation problems or where trees need to store charcters like dictionary
# 2.Fast lookups of character
# 3. The class of this strcuture contains a HashMap to map the nodes to their
# respective characters node[2]='a' and also each node has a boolena called isComplete
# This tells if there is a complete word at the end of the current node. Usually this
# flag is attached as a special character ot the left or riht child of the node
# like node[2.left]='*'
# 4. The lookup of Trie and Hashmap is same as O(n), the difference is space. Trie takes less
# space as it doesn't store the individual words but their prefix. Like
# subset,subtree= 7+6 but in Trie= 7+3

#------------ Special Printing using Level Order Traversal Trees----------#
# 1.currentCount=Records the number of nodes to prin in a level
# 2. nextCount=Records the number of nodes in a level
# 3. Here used stack as well to print upside down
#class Node:
#    def __init__(self,data):
#        self.data=data
#        self.left=None
#        self.right=None
#    
#def levelOrderTraversal(node):
#    queue=[node]
#    currentCount=1
#    nextCount=0
#    opposite=[]
#    
#    while queue:
#        currentNode=queue.pop() 
##        print(currentNode.data,end=' ')
#        opposite.append(currentNode.data)
#        currentCount-=1 # With each node on the same level this is reduced by 1
#        if(currentNode.left!=None):
#            queue.append(currentNode.left)
#            nextCount+=1        # Counts the total number of nodes in a level by incrementing
#        if(currentNode.right!=None):
#            queue.append(currentNode.right)
#            nextCount+=1
#        if(currentCount==0): # If all the nodes are printed on a level, the next count will tell how many nodes to print for the next level
#            opposite.append(',')
#            currentCount,nextCount=nextCount,currentCount
#    print(opposite)  
#    for i in opposite[::-1]:
#        if(i==','):
#            print('\n')
#        else:
#            print(i,end=' ')
#        
#root = Node(1) 
#root.left = Node(2) 
#root.right = Node(3) 
#root.left.left = Node(4) 
#root.left.right = Node(5)
#root.left.left.right = Node(6)  
#root.left.left.left = Node(7)  
#levelOrderTraversal(root) 

#------------- Revision-----------#

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def add(root,value):
    if(value<root):
        if(root.left==None):
            root.left=Node(value)
        else:
            add(root.left,value)
    if(value>root):
        if(root.right==None):
            root.right=Node(value)
        else:
            add(root.right,value)
            
def traveral_1(root,value):
    if(value==root):
        print("Yes")
    else:
        if(root.left==None and root.right==None):
            return False
        if(value<root):
            traveral_1(root.left,value)
        elif(value>root):
            traveral_1(root.right,value)
    
def levelOrder(root):
    queue=[root]
    while queue:
        currentNode=queue.pop(0)
        print(currentNode)
        if(currentNode.left!=None):
            queue.append(currentNode.left)
        if(currentNode.right!=None):
            queue.append(currentNode.right)
            
def traversal_2(root,counter,val):
    if root==val:
        return root
    if(root==None):
        return None
    else:
        left=traversal_2(root.left,counter+1)
        right=traversal_2(root.right,counter+1)
        if(left==val and right==val):
            return root
        if(left):
            return left
                    
def traversal_3(root,val,counter):
    if(root==None):
        return 1
    else:
        left=traversal_2(root.left)
        right=traversal_2(root.righ)
        counter=counter+left+right
    return counter

        
      
        
        


        
        
        
        
        
        


