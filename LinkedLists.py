#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:18:47 2020

@author: ronaksharma
"""



#-----------LINKED LIST----------#
# Set of nodes which contain their own values and link to the next nodes. The Class
# LinkedList contains an object of Class Node
# Always check if an OBJECT EXISTS and not its ATTRIBUTE like Node!=None than Node.data!=None
# 1. Takes linear time to traverse and find a variable
# 2. Insertion and Deletion can be done in O(1)
# 3. However appending at the end will again take very long
# 4. Single Linked List: Elements connected moving foward
# 5. Double Linked List: Elements connected both ways
# 6. Used to make circular arrays. Traverse throgh the whole list from any node
# not from the head. Just remember the starting point, node.next != starting_point
# 7. Update headpointer each time you change the pointer or delete it. Just changing
# the reference ot the next node deletes the head
#----- Example------#
# 1. ALways three conditions, at beginning , end and the middle. 
# Alwyas compare the current and the front value. Easier to understnad

#class Node:
#    def __init__(self,data):
#        self.data=data
#        self.next=None
#        
#class LinkedList:
#    
#    def __init__(self,nodes=None):
#        self.head=None
#        if nodes!= None:
#            node=Node(data=nodes.pop(0))
#            self.head=node
#            for elements in nodes:
#                node.next=Node(data=elements)
#                node=node.next
#                
#    def traverse(self):
#        node=self.head
#        while node is not None:
#            print(node.data)
#            node=node.next
#            
#    def add_first(self,node):
#        node.next=self.head
#        self.head=node
#            
#llist = LinkedList(["a", "b", "c", "d", "e"])          
      

#l.traverseList(l.head)

#-----1----------#

#---2------Inserting element in a Sorted Double Linked List-------#
# 1. Always return the HEAD and in cases where the head will change, return a new head
# If not return either it counts from the old head or the continue to do the rest of the procesing
#
#def sortedInsert(head, data):
#    temp_node=head
#    reachedEnd=0
#    while(data>temp_node.data):
#        if(temp_node.next):
#            temp_node=temp_node.next
#        else:
#            reachedEnd=1
#            break
#    foundPosition=DoublyLinkedListNode(data)
#    print(reachedEnd)
#    if(reachedEnd==1):
#        temp_node.next=foundPosition
#        foundPosition.prev=temp_node
#        return head
#    
#    previousNode=temp_node.prev
#    if(previousNode):
#        previousNode.next=foundPosition
#        foundPosition.prev=previousNode
#        foundPosition.next=temp_node
#        temp_node.prev=foundPosition
#    else:
#        foundPosition.next=temp_node
#        temp_node.prev=foundPosition
#        return foundPosition
#
#    return heads

#----3.----- Reversing a Doubled Linked List------#
# 1. Each time you move forward keep on remembering the new head value
# 2. After swapping the trick is to move backwards and not forwards
#def reverse(head):
#    temp_node=head
#    while(temp_node):
#        temp_node.next,temp_node.prev=temp_node.prev,temp_node.next
#        new_head=temp_node
#        temp_node=temp_node.prev


#---4--------Remove Linked List Nodes-------#
# 1. Update the head always and store the previous node beofre entering the if condition
#            prev = cur
#            cur = cur.next
#            if (cur.data == key):
#                prev.next = cur.next
#                return

#------5-----------Merge Point Linked List----#
# 1. VERY IMPORTANT
# Assume traversing len x and point of merge j and list y point of merge k
# So for List 1 
# length covered= j(reached merge point) + (x-j)(reached end)+k(merge point of other list)
# For list 2, totoal length = k + y-k +j
# Now since lists merge so distance of x-j and y-k are equal. Substituting as q in above
# list 1= j+q+k and list 2= k+q+j, Therefore this gives us the merge point
#def findMergeNode(headA, headB):
#    curA = headA
#    curB = headB
#    while curA != curB:
#        if curA.next == None:
#            curA = headB
#        else:
#            curA = curA.next
#
#        if curB.next == None:
#            curB = headA
#        else:
#            curB = curB.next
#    return curB.data

#------------- Revision-----------#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class linkedList:
    
    def __init__(self,nodes):
        self.head=None
        if(nodes!=None):
            node=nodes.pop(0)
            self.head=Node(data=node)
            self.head.prev=None
            for i in nodes:
                self.head.next=Node(data=i)
                prev=self.head
                self.head=self.head.next
                self.head.prev=prev
        
        
    def removeNode(self,val,curr):
        prevNode=curr
        curr=curr.next
        if(curr.data==val):
            prevNode.next=curr.next
        curr.prev=prevNode.prev
        prevNode.next
            