class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        dq = collections.deque([root])
        result = 0

        while dq:
            level = len(dq)

            for i in range(level):
                node = dq.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
        return result
