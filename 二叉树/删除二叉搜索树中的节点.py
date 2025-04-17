class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # 找到右子树中最小的节点
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 将被删除节点的左子树接到这个最小节点上
                cur.left = root.left
                # 返回右子树作为新的根节点
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root 
