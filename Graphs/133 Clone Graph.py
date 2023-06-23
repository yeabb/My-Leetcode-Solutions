"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        

        def dfs(node):
            if not node:
                return None

            if node in oldToNew:
                return oldToNew[node]

            copy=Node(node.val)
            oldToNew[node]=copy
            for nbrs in node.neighbors:
                copy.neighbors.append(dfs(nbrs))
            return copy

        oldToNew={}
        return dfs(node)
        
            


        
       