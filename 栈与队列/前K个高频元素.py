class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import heappop, heappush

        nums_counter = Counter(nums)
        min_heap = []

        for val, count in nums_counter.items():
            heappush(min_heap, (count, val))

            if len(min_heap) > k:
                heappop(min_heap)
        
        return [num for _, num in min_heap]
