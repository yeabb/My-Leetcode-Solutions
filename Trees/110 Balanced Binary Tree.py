# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [-1, True]

            leftHeight=dfs(node.left)
            rightHeight=dfs(node.right)
            

            if leftHeight[1]==False or rightHeight[1]==False or abs(leftHeight[0]-rightHeight[0])>1:
                return [0, False]

            return [max(leftHeight[0], rightHeight[0])+1, True]
        return dfs(root)[1]

