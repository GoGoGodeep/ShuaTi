def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    result = 0
    min_len = float('inf')

    for right in range(len(nums)):
        result += nums[right]

        while result >= target:
            min_len = min(min_len, right - left + 1)
            result -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
