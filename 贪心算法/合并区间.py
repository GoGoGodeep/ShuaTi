class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        
        if len(intervals) == 0:
            return result
        
        intervals.sort(key=lambda x:x[0])

        result.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:    # 发现重叠
                # 合并区间
                result[-1][1] = max(intervals[i][1], result[-1][1])     
            else:
                result.append(intervals[i])     # 区间不重叠

        return result
