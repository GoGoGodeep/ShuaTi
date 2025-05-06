class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return 1 * (n - 1)

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[i - j] * dp[j])

        return dp[n]
