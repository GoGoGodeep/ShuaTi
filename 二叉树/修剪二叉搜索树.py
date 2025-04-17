class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 迭代法一：
        # if not root:
        #     return None
        
        # # 处理头节点，让root移动到[low, high]的范围内，注意是左闭右闭
        # while root and (root.val < low or root.val > high):
        #     if root.val < low:
        #         root = root.right   # 小于low，往右走
        #     else:
        #         root = root.left    # 大于high，往左走
        
        # cur = root
        # # 此时root已经在[low, high]范围内，处理左孩子元素小于low的情况
        # while cur:
        #     while cur.left and cur.left.val < low:
        #         cur.left = cur.left.right
        #     cur = cur.left
        
        # cur = root
        # # 此时root已经在[low, high]范围内，处理右孩子元素大于high的情况
        # while cur:
        #     while cur.right and cur.right.val > high:
        #         cur.right = cur.right.left
        #     cur = cur.right
        
        # return root

        # 迭代法二：
        if not root:
            return None
        
        if root.val < low:
            # 寻找符合区间 [low, high] 的节点
            return self.trimBST(root.right, low, high)
        if root.val > high:
            # 寻找符合区间 [low, high] 的节点
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)      # root.left 接入符合条件的左孩子
        root.right = self.trimBST(root.right, low, high)    # root.right 接入符合条件的右孩子

        return root
