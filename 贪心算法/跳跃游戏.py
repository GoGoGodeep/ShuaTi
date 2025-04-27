class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        for i in range(len(nums)):
            if i <= curr:
                curr = max(curr, i + nums[i])

                if curr >= len(nums) - 1:
                    return True
            
            else:       # 如果当前的索引大于了curr，说明已无法到达索引的位置
                return False
