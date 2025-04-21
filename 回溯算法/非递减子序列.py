class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if len(path) > 1:
                result.append(path[:])

            used = set()
            for i in range(start, len(nums)):
                if path and nums[i] < path[-1]:
                    continue
                if nums[i] in used:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result
