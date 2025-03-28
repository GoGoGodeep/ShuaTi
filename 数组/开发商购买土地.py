n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 计算行和列的总和
row_sums = [sum(row) for row in grid]
col_sums = [0] * m
for i in range(n):
    for j in range(m):
        col_sums[j] += grid[i][j]

# 总价值
S = sum(row_sums)

# 计算前缀和
prefix_row = [0]
current = 0
for rs in row_sums:
    current += rs
    prefix_row.append(current)

prefix_col = [0]
current = 0
for cs in col_sums:
    current += cs
    prefix_col.append(current)

# 处理横向分割
min_horizontal = float('inf')
for k in range(1, n):
    diff = abs(S - 2 * prefix_row[k])
    if diff < min_horizontal:
        min_horizontal = diff

# 处理纵向分割
min_vertical = float('inf')
for l in range(1, m):
    diff = abs(S - 2 * prefix_col[l])
    if diff < min_vertical:
        min_vertical = diff

# 取最小值
print(min(min_horizontal, min_vertical))
