class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, remaining_sum):
            if remaining_sum == 0 and len(path) == k:
                result.append(path[:])
                return

            if remaining_sum <= 0 or len(path) >= k:
                return
            
            for i in range(start, 10):
                if i > remaining_sum:
                    break
                path.append(i)
                backtrack(i+1, path, remaining_sum - i)
                path.pop()
        
        backtrack(1, [], n)
        return result


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if sum(path) == n and len(path) == k:
                result.append(path[:])
              
            for i in range(start, 10):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        
        backtrack(1, [])

        return result
