class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = []

        def get(node):
            if not node:
                return
            get(node.left)
            result.append(node.val)
            get(node.right)
        
        get(root)

        if len(result) < 2:
            return 0
        
        final = float('inf')
        for i in range(1, len(result)):
            final = min(final, result[i] - result[i-1])
        
        return final
