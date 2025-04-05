class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        dq = deque()
        result = []

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if right - k + 1 > dq[0]:
                dq.popleft()
            
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
