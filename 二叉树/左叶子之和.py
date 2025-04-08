# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return 
            
            if node.left:
                if not node.left.left and not node.left.right:
                    self.result += node.left.val
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return self.result
