# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        从下往上安装摄像头

        0：该节点未覆盖
        1：该节点有摄像头
        2：该节点有覆盖
        """

        self.result = 0
   
        def dfs(cur):
            if not cur:
                return 2
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            # 情况1：左右节点都有覆盖
            if left == 2 and right == 2:
                return 0

            # 情况2：
            # left == 0 && right == 0 左右节点无覆盖
            # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
            # left == 0 && right == 1 左节点无覆盖，右节点有摄像头
            # left == 0 && right == 2 左节点无覆盖，右节点覆盖
            # left == 2 && right == 0 左节点覆盖，右节点无覆盖
            if left == 0 or right == 0:
                self.result += 1
                return 1
            
            # 情况3:
            # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
            # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
            # left == 1 && right == 1 左右节点都有摄像头
            if left == 1 or right == 1:
                return 2

        if dfs(root) == 0:
            self.result += 1

        return self.result
