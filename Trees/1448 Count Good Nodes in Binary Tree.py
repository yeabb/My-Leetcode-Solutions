# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node):
            
            if node.left:
                if node.left.val>=node.val:
                    res.append(node.left.val)
                node.left.val=max(node.left.val, node.val)
                dfs(node.left)
            if node.right:
                if node.right.val >= node.val:
                    res.append(node.right.val)
                node.right.val=max(node.right.val, node.val)
                dfs(node.right)
            return

        if not root:
            return 0
        res=[root.val]
        dfs(root)
        return len(res)



