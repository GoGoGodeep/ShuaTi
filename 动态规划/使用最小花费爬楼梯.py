class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [1 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        # 最后一步理解为不用花费，所以取倒数第一步、第二步的最小值
        return min(dp[-1], dp[-2])
