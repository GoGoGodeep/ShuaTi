# https://mp.weixin.qq.com/s/BjYgrBwnCnq32UXeuSaVsg

def compute_coordinates(n):
    """ 计算二叉树中每个节点的坐标 """
    coordinates = {1: (0, 0)}  # 根节点坐标
    for i in range(2, n + 1):
        parent = i // 2  # 父节点编号
        a, b = coordinates[parent]  # 获取父节点坐标
        if i % 2 == 0:
            coordinates[i] = (a - 1, b - 1)  # 左子节点
        else:
            coordinates[i] = (a + 1, b - 1)  # 右子节点
    return coordinates

def manhattan_distance(coord1, coord2):
    """ 计算曼哈顿距离 """
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)

def process_queries(n, queries):
    """ 计算所有查询的曼哈顿距离 """
    coordinates = compute_coordinates(n)
    results = []
    for u, v in queries:
        results.append(manhattan_distance(coordinates[u], coordinates[v]))
    return results

# 示例用法
if __name__ == "__main__":
    n = int(input("请输入树的节点数: "))
    q = int(input("请输入查询次数: "))
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    results = process_queries(n, queries)
    for res in results:
        print(res)
