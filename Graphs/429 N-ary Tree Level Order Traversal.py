from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []

        q=deque()
        q.append(root)
        res=[]
        while(q):
            qLen=len(q)
            level=[]
            for i in range(qLen):
                root=q.popleft()
                q.extend(root.children)
                level.append(root.val)

            if level:
                res.append(level)

        return res