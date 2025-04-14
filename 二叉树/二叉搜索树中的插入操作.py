class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # # 递归
        # if not root:
        #     node = TreeNode(val)
        #     return node
        
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # if root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)
        
        # return root

        # 迭代
        if not root:
            return TreeNode(val)
        
        cur = root

        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur = cur.left
            elif val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                else:
                    cur = cur.right
