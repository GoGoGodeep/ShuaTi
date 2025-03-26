def sortedSquares(self, nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    result = []

    while left <= right:
        temp_left = nums[left] ** 2
        temp_right = nums[right] ** 2
        if temp_left > temp_right:
            result.append(temp_left)
            left += 1
        else:
            result.append(temp_right)
            right -= 1
    
    return result[::-1]
