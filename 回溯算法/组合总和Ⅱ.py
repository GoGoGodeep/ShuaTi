class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(start, path, total):
            if sum(path) == target:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # 保证不出现重复数字
                """
                候选数组包含重复数字
                例如：candidates = [1,1,2,5]，target = 8
                排序后仍然是 [1,1,2,5]
                如果不跳过重复的 1，回溯过程可能会选择两次 1（来自不同的位置），导致生成 [1,2,5] 两次：
                
                第一次选 candidates[0]（第一个 1），然后选 2 和 5
                第二次选 candidates[1]（第二个 1），然后选 2 和 5
                这样结果里会有两个 [1,2,5]，但实际上它们是相同的组合。
                """
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if total + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i+1, path, total+candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result
