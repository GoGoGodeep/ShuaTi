class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has_set = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in has_set:
                return [has_set[target - nums[i]], i]
            else:
                has_set[nums[i]] = i
