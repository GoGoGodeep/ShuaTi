class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        curr = 0
        pre = 0
        result = 1

        for i in range(len(nums) - 1):
            curr = nums[i + 1] - nums[i]
            if (pre <= 0 and curr > 0) or (pre >= 0 and curr < 0):
                result += 1
                pre = curr
        
        return result
