def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    left = top = 0
    right = bottom = n - 1
 
    num = 1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    return matrix
