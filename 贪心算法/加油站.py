class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = 0    # 当前累计的剩余油量
        total = 0   # 总剩余油量
        start = 0   # 起始位置

        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if curr < 0:
                start = i + 1
                curr = 0

        if total < 0:
            return -1
        
        return start
