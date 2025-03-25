def removeElement(self, nums: List[int], val: int) -> int:
    # 快慢指针法
    fast = slow = 0
    
    while fast < len(nums):     # 不加等于是因为，a = size 时，nums[a] 会越界
        # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    
    return slow
