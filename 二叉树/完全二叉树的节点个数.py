# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        dq = collections.deque([root])

        while dq:
            level = len(dq)

            for _ in range(level):
                node = dq.popleft()
                result += 1

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return result

# 递归
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
