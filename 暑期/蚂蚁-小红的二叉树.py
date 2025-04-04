# https://mp.weixin.qq.com/s/BjYgrBwnCnq32UXeuSaVsg

from collections import deque
import sys

input = sys.stdin.readline

# 读入节点数和查询数
n, q = map(int, input().split())
tree = [[] for _ in range(n+1)]

# 构造树（无向图）
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

x_coord = [0] * (n + 1)
y_coord = [0] * (n + 1)

def bfs(root):
    dq = deque()
    dq.append((root, 0))    # (当前节点, 父节点)

    while dq:
        node, parent = dq.popleft()
        children = sorted([
            v for v in tree[node] if v != parent
        ])

        for i, child in enumerate(children):
            if i == 0:  # 左儿子
                x_coord[child] = x_coord[node] - 1
                y_coord[child] = y_coord[node] - 1
            else:       # 右儿子
                x_coord[child] = x_coord[node] + 1
                y_coord[child] = y_coord[node] - 1
            dq.append((child, node))

# 计算树的坐标
bfs(1)

# 处理查询
output = []
for _ in range(q):
    u, v = map(int, input().split())
    output.append(str(abs(x_coord[u] - x_coord[v]) + abs(y_coord[u] - y_coord[v])))

sys.stdout.write("\n".join(output) + "\n")
