class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照h维度的身高顺序从高到低进行排序，确定第一个维度
        # 当-x[0]（维度h）相同时，再根据x[1]（维度k）从小到大排序
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []

        # 根据每个元素的第二个维度k，使用贪心算法进行插入
        # people已经进行排序，同一高度时k值小的排前面
        for i in people:
            result.insert(i[1], i)
        
        return result
