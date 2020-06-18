#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:41:34 2020

@author: ronaksharma
"""

#----------Graphs----------#
# Graphs can contain cycle and trees don't
# All Graphs are considered bi-directional
# 1. DFS: Deep to children than neighbour, O(V), Edge based,Uses Stacks
# 2. defaultdict: One Key has a list of values associated with it
# 3. Graph should have unique vertices to apply DFS/BFS
# 4. To traverse a disconnected graphs, you need to run another function
# running DFS on all vertices rather than just once
# 5. In DFS and BFS, no NODE property. These are just numbers. No node.data exists

#--------------RECURSIVE METHOD----------------#
#from collections import defaultdict
##
#class Graph:
#    
#    def __init__(self):
#        self.graph=defaultdict(list)
#    
#    def addEdge(self,u,v):
#        self.graph[u].append(v)
#        self.graph[v].append(u)
#    
#    def execDFS(self,v,visited):
#        if v not in visited:
#            print(v)
#            visited.append(v)
#            for i in self.graph[v]:
#                self.execDFS(i,visited)
#
#    def DFS(self,v):
#        visited=[]
#        self.execDFS(v,visited)
#
#g=Graph()
#g.addEdge(0, 1) 
#g.addEdge(0, 2) 
#g.addEdge(1, 0) 
#g.addEdge(2, 0) 
#print("Following is DFS from (starting from vertex 2)") 
#g.DFS(0)
#--------------ITERATIVE METHOD------------#
#def dfs(graph, node):
#    visited = [node]
#    stack = [node]
#    while stack:
#        node = stack,pop()
#        if node not in visited:
#            visited.extend(node)
#            print(node)
#        remove_from_stack = True
#        for next in graph[node]:
#            if next not in visited:
#                stack.extend(next)
#                remove_from_stack = False
#                break
#        if remove_from_stack:
#            stack.pop()
#    return visited
#graph = {'A': ['B', 'C', 'E'],
#         'B': ['A','D', 'E'],
#         'C': ['A', 'F', 'G'],
#         'D': ['B'],
#         'E': ['A', 'B','D'],
#         'F': ['C'],
#         'G': ['C']}
#dfs(graph,'A')


# -1.----- Connected Cell in a Grid-------------#
# 1. Continue: When condition is satisfied, skip the iteration
# 2. When a LOCAL variable is assigned in recurssion its values is different in each DFS
# Counting when bubbling up, use x=DFS() and return  x+=DFS()
# 3. If a variable is assigned GLOBAL or PASSED AS REFERNCE it can be changed accross all DFS
#. So to count when bubble down, use GLOBAL and pass it as an argument in DFS(counter+1)
#def DFS(grid,gridRow,gridColumn,visited):
#    count=0
#    if((gridRow,gridColumn) not in visited):
#        visited.append((gridRow,gridColumn))
#
#        if(grid[gridRow][gridColumn]==0):
#            return 0
#        count=1
#        
#        for row in range(-1,2):
#            if((gridRow==0 and row==-1) or(gridRow==(len(grid)-1)    and row==1)):
#                continue
#            for column in range(-1,2):
#                if((gridColumn==0 and column==-1) or (gridColumn==(len(grid[0])-1) and column==1)):
#                    continue
#                count+=DFS(grid,gridRow+row,gridColumn+column,visited)
#                
#    return count
#def maxRegion(grid):
#    visited=[]
#    maxFound=0
#    for i in range(len(grid)):
#        for j in range(len(grid[0])):
#            maxFound=max(maxFound,DFS(grid,i,j,visited,maxFound))
#    return maxFound
#
#k=[[0,0,1,1],[0, 0, 1, 1,]]
#result=maxRegion(k)
#print(result)


#--------- BREADTH FIRST SEARCH-----------#
#def BFS(graph,visited,queue,node):
#    visited.append(node)
#    queue.append(node)
#    
#    while queue:
#        currentNode=queue.pop(0)
#        print(currentNode,end=' ')
#        for neighbours in graph[currentNode]:
#            if(neighbours not in visited):
#                visited.append(neighbours)
#                queue.append(neighbours)
#
#def applyBFS(graph,node):
#    visited=[]
#    queue=[]
#    BFS(graph,visited,queue,node)
#
#        
#
##graph = {'A': ['B', 'C', 'E'],
##         'B': ['A','D', 'E'],
##         'C': ['A', 'F', 'G'],
##         'D': ['B'],
##         'E': ['A', 'B','D'],
##         'F': ['C'],
##         'G': ['C']}
#graph={1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2], 5: [3]}
#
#applyBFS(graph,1)

#-2.-------- Shortest Reach in Graph----------#
# 1. To count values bubbling down, use the parent nodes values as that remains constant in a level or sizee of queue
#from collections import defaultdict,OrderedDict
#
#class Graph:
#    
#    def __init__(self,numberOfNodes):
#        self.graph=defaultdict(list)
#        self.numberOfNodes=numberOfNodes
#        
#    
#    def connect(self,u,v):
#        self.graph[u].append(v)
#        self.graph[v].append(u)
#        
#
#    def BFS(self,visited,queue,node):
#        occurence=0
#        self.nodesOccurenceDict=dict()
#        self.nodesOccurenceDict[node]=0
#        visited.append(node)
#        queue.append(node)
#        while queue:
#            currentNode=queue.pop(0)
##            print(currentNode,' ')
#            for neighbour in self.graph[currentNode]:
#                if neighbour not in visited:    
#                    occurence=self.nodesOccurenceDict[currentNode]+6
#                    self.nodesOccurenceDict[neighbour]=occurence
#                    visited.append(neighbour)
#                    queue.append(neighbour)
#        del self.nodesOccurenceDict[node]
#        self.attachTheMissingNode(self.nodesOccurenceDict,node)
#            
#    def attachTheMissingNode(self,nodesDictionary,node):
#        sizeOfNodes=self.numberOfNodes
#        for i in range(1,sizeOfNodes+1):
#            if (i not in nodesDictionary) and (i!=node):
#                nodesDictionary[i]=-1
#        OrderedDict(sorted(self.nodesOccurenceDict.items(), key=lambda t: t[0]))
#        
#            
#    def printOccurence(self):
#        finalResultList=(list(self.nodesOccurenceDict.values()))
#        finalResult=' '.join(map(str,finalResultList))
#        print(finalResult)
#                    
#g=Graph(6)
#g.connect(1,2)
#g.connect(1,3)
#g.connect(3,4)
#g.connect(2,5)
#visited=[]
#queue=[]
#node=1
#g.BFS(visited,queue,node)
#g.printOccurence()


#-------Even Tree-----#
# 1. UniDirect graphs are connected both ways. So if A->B, then also add B->A

#from collections import defaultdict
#def evenForest(t_from, t_to):
#    graph=defaultdict(list)
#    for i in range(len(t_to)):
#        graph[t_to[i]].append(t_from[i])
#    root=1
#    counter=0
#    DFS(graph,root,counter)
#    return maxCounter
#
#maxCounter=-1
#def DFS(graph,node,counter):
#    global maxCounter
#    if(len(graph[node])==0):
#        return 1
#    else:
#        result=1
#        for vertex in graph[node]:
#            result=result+DFS(graph,vertex,counter+1)
#    print(vertex,result)
#    if(result%2==0):
#        maxCounter+=1
#    return result
#    
#
#x=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #x to y
#y=[1, 1, 3, 2, 1, 2, 6, 8, 8, 10, 10, 9, 12, 12]
#result=evenForest(x,y)
#print(result)

#---------------Nearest Clone-------------#
# 1. Use the parent node height to calculate the height of the child in DFS or BFS
# 2. Two find the shortest between two nodes, start BFS from one of those nodes
# 3. In BFS any checks for the node value, like the colour or if it s 1 or 0 should be don outside the for loop
#from collections import defaultdict
#
#def findShortest(graph_nodes, graph_from, graph_to, ids, val):
#    graph=defaultdict(list)
#    for i in range(len(g_to)):
#        graph[g_to[i]].append(g_from[i])
#        graph[g_from[i]].append(g_to[i])
#    node=ids.index(val)+1
#    levelOfNode=searchGraph(graph,ids,val,node)
#    return levelOfNode
#
#def searchGraph(graph,ids,val,node):
#    if val not in ids:
#        return -1
#    elif ids.count(val)==1:
#        return -1
#    else:
#        queue=[node]
#        visited=[node]  
#        level={node:0}
#        while queue:
#            currentNode=queue.pop(0)
#            for neighbour in graph[currentNode]:
#                if neighbour not in visited:
#                    level[neighbour]=level[currentNode]+1
#                    queue.append(neighbour)
#                    visited.append(neighbour)
#            if(ids[currentNode-1]==val and currentNode!=node):
#                return level[currentNode]
#
#graph_nodes=4
#g_from=[1,1,4]
#g_to=[2,3,2]
#ids=[1,2,1,1]
#val=1
#outcome=findShortest(graph_nodes,g_from,g_to,ids,val)
#print(outcome)

#------------- Revision-----------#
arr={1:[1,2,3,4],2:[4,5,6]}
     
def mainFunction(root,graph,nodes,value):
    visited=[]
    for i in range(nodes):
        DFS(graph,value,i,visited)
    
def DFS(graph,value,root,visited):
    if root not in visited:
        visited.append(root)
        if(root.data==0):
            return 0
        counter=1
        for neighbours in graph[root]:
                counter=counter+DFS(graph,value,neighbours,visited,counter)
        return counter        
                
def BFS(graph,value,root,visited,queue):
    queue=[root]
    visited=[root]
    level={root:0}
    while queue:
        node=queue.pop(0)
        print(node) 
        for neigh in graph[node]:
            if neigh not in visited:
                level[neigh]=level[node]+1
                queue.append(neigh)
                visited.append(neigh)
            
    
def tree_dfs(graph,node,counter):
    global maxCounter
    if(len(graph[node])==0):
        return 0
    else:
        result=1
        for vertex in graph[node]:
            result=result+tree_dfs(graph,vertex,counter+1)
    print(vertex,result)
    if(result%2==0):
        maxCounter+=1
    return result




