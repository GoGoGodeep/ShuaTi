class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()    # 胃口值从小到大
        s.sort()    # 饼干尺寸从小到大

        child = 0       # 当前要尝试满足的孩子  
        cookie = 0      # 当前可用的饼干
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
            
        return child
