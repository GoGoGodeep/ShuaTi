class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0
        if (target + total_sum) % 2 == 1:
            return 0
        
        target_sum = (target + total_sum) // 2      # 目标和

        dp = [0] * (target_sum + 1)     
        dp[0] = 1   # 当目标和为0时，只有一种方案，即什么都不选

        for num in nums:
            for j in range(target_sum, num - 1,  -1):
                dp[j] += dp[j - num]    # 状态转移方程，累加不同选择方式的数量
        
        return dp[target_sum]
