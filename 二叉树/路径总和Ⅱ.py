class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        result = []

        def dfs(node, curr):
            if not node:
                return
            
            curr -= node.val
            path.append(node.val)
            if not node.left and not node.right and curr == 0:
                result.append(path[:])
            
            dfs(node.left, curr)
            dfs(node.right, curr)
            path.pop()
        
        dfs(root, targetSum)
        return result
