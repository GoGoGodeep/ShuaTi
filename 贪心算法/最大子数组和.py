class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            if curr > result:
                result = curr
            if curr <= 0:
                curr = 0
        return result
