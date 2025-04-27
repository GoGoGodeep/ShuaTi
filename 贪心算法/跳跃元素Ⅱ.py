class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_distance = 0
        result = 0
        next_distance = 0

        for i in range(len(nums) - 1):  # 不需要从最后一个元素起跳，题目已经保证一定可以到达最后一个元素
            next_distance = max(next_distance, i + nums[i])
            
            if i == curr_distance:  # 如果当前索引等于curr_distance，说明当前无法到达最终元素
                curr_distance = next_distance
                result += 1
            
        return result
