class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1        

        dp = [1 for _ in range(n)]
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[-1]
