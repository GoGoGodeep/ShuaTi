class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for stone in stones:
            for j in range(target, stone - 1, -1):
                # 判断当前重量是否可以通过选择之前的石头得到或选择当前石头和之前的石头得到
                dp[j] = dp[j] or dp[j - stone]

        for i in range(target, -1, -1):
            if dp[i]:
                # 返回剩余石头的重量，即总重量减去两倍的最接近总重量一般的重量
                return total - 2 * i
