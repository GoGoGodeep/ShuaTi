# 移除元素的双指针实现
# 快慢指针实现见https://github.com/GoGoGodeep/ShuaTi/blob/main/%E6%95%B0%E7%BB%84/%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            
            while left <= right and nums[right] == val:
                right -= 1
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return left
