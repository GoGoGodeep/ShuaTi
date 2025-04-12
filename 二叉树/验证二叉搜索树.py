class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False

            return True
        
        return dfs(root)
