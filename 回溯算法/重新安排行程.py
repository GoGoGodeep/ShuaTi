class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        
        # 构建图的邻接表，并按字典序逆序排序
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # 对每个出发机场的到达列表进行逆序排序
        for src in graph:
            graph[src].sort(reverse=True)

        def backtrack(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                backtrack(next_airport)
            result.append(airport)
        
        backtrack('JFK')
        return result[::-1]
