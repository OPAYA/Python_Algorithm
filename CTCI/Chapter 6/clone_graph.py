"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloneG = {}
        
        def DFS(node):
            if node not in cloneG:
                cloneG[node] = Node(node.val, None)
                cloneG[node].neighbors = [DFS(n) for n in node.neighbors]
            return cloneG[node]
        
        DFS(node)
        return cloneG[node]