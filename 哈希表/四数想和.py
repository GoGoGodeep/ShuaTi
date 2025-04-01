class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import defaultdict

        has_set = defaultdict(int)
        for i in nums1:
            for j in nums2:
                has_set[i + j] += 1

        result = 0
        for x in nums3:
            for y in nums4:
                if -x-y in has_set:
                    result += has_set[-x-y]

        return result
