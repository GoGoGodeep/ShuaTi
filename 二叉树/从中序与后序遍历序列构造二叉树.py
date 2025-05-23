class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 第一步：递归终止条件
        if not postorder:
            return None
        
        # 第二步：后序遍历的最后一个就是当前的中间节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步：找切割点
        idx = inorder.index(root_val)

        # 第四步：切割inorder数组，得到inorder数组的左、右半边
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        # 第五步：切割postorder数组，得到postorder数组的左右半边
        # 重点：中序数组大小一定跟后序数组大小相同
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder) - 1]

        # 第六步：递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
