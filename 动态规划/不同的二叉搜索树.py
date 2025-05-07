class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1   # 当n为0时，只有一种情况，即空树，所以dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):   # 对于每个数字i，计算以i为根节点的二叉搜索树的数量
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[-1]
