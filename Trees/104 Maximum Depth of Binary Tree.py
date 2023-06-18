# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
    #Bottom Up recurssion solution-----------------------
    
#         if(not root):
#             return 0

#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    #BFS solution -----------------------------------
    
        q=collections.deque()
        q.append(root)
        res=0
        while q:
            qLen=len(q)
            levelExist=False
            for i in range(qLen):
                node=q.popleft()
                if node:
                    levelExist=True
                    q.append(node.left)
                    q.append(node.right)
            if levelExist:
                res+=1
        return res