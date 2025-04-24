class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
 
        def is_valid(row, col):
            # 检查列
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False        # 当前列已经存在皇后，不合法
            
            # 检查 45 度角是否有皇后
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False    # 左上方向已经存在皇后，不合法
                i -= 1
                j -= 1

            # 检查 135 度角是否有皇后
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == 'Q': 
                    return False    # 右上角已经存在皇后，不合法
                i -= 1
                j += 1
            
            return True

        def backtrack(row):
            if row == n:
                result.append([''.join(row) for row in chessboard])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    chessboard[row][col] = 'Q'
                    backtrack(row+1)
                    chessboard[row][col] = '.'
        
        backtrack(0)
        
        return result
