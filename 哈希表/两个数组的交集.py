class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict

        has_set = defaultdict(int)
        for num in nums1:
            has_set[num] += 1

        result = []
        for num in nums2:
            if num in has_set:
                result.append(num)
                del has_set[num]

        return result
