class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        path = []

        def backtrack(index):
            if index == len(digits):
                result.append("".join(path))
                return

            digit = digits[index]
            for i in nums[digit]:
                path.append(i)
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        return result
