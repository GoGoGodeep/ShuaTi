class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        # # 优化
        # def backtrack(start, path):
        #     if start == len(s):
        #         result.append(path)
        #         return

        #     for end in range(start+1, len(s)+1):
        #         sub = s[start:end]

        #         if sub == sub[::-1]:
        #             backtrack(end, path + [sub])

        # 未优化
        def is_true(s):
            return s == s[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
            
            for end in range(start+1, len(s)+1):
                sub = s[start:end]

                if is_true(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return result
