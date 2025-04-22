class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False for _ in range(len(nums))]

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                # 剪枝条件：当前数字与前一个数字相同，且前一个数字未被使用过
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        
        backtrack([])
        return result
