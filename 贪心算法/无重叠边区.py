class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:   # 重叠
                result += 1
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1]) # 更新边界

        return result
