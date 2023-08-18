# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None
            if node.val == p.val or node.val==q.val:
                return node
            
            
            leftNode = None if node.val < p.val and node.val < q.val else dfs(node.left)
            rightNode = None if node.val > p.val and node.val > q.val else dfs(node.right)

                

            if not leftNode and not rightNode:
                return None
            elif rightNode and not leftNode:
                return rightNode
            elif leftNode and not rightNode:
                return leftNode
            else:
                return node

        return dfs(root)