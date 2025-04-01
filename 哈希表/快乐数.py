class Solution:
    def isHappy(self, n: int) -> bool:
        has_set = set()
        
        def cal(n):
            result = 0
            while n:
                result += (n % 10) ** 2
                n //= 10
            
            if result == 1:
                return True
            
            if result not in has_set:
                has_set.add(result)
            else:
                return False
            
            return cal(result)

        return cal(n)
