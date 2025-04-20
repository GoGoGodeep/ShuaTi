class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(start, path, total):
            if sum(path) == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result
