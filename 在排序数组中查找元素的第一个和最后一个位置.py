# 还是leetcode的写法简单

def getleft():
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
        return left


def getright():
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
        return right

left = getleft()
right = getright()

if left <= right:
    return [left, right]
else:
    return [-1, -1]
