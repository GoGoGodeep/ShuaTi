class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        i = 0

        while i <= curr:
            curr = max(curr, i + nums[i])

            if curr >= len(nums) - 1:
                return True
            
            i += 1

        return False
