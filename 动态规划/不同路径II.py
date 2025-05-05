class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1

        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[-1][-1]
