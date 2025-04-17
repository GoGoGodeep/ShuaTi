class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 处理头节点，让root移动到[low, high]的范围内，注意是左闭右闭
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right   # 小于low，往右走
            else:
                root = root.left    # 大于high，往左走
        
        cur = root
        # 此时root已经在[low, high]范围内，处理左孩子元素小于low的情况
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        
        cur = root
        # 此时root已经在[low, high]范围内，处理右孩子元素大于high的情况
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        
        return root
