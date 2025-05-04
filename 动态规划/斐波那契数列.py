class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        result = [1 for _ in range(n)]

        for i in range(2, n):
            result[i] = result[i-1] + result[i-2]

        return result[-1]
