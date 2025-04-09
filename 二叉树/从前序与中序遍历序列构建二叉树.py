class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 从前序与中序遍历序列构造二叉树
        # 第一步：终止条件
        if not preorder:
            return None
        
        # 第二步：前序遍历的第一个就是当前的中间节点。
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 第三步：找切割点
        idx = inorder.index(root_val)

        # 第四步：切割inorder数组，得到inorder数组的左、右半边。
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        # 第五步：切割preorder，得到preorder数组的左、右半边
        # 重点：中序数组大小一定跟前序数组的大小相同。
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # 第六步：递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
