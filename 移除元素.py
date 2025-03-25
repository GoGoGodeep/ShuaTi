def removeElement(self, nums: List[int], val: int) -> int:
    # 快慢指针法
    fast = slow = 0
    
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    
    return slow
