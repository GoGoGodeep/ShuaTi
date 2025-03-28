"""
题目描述：
给定一个整数数组 Array，请计算该数组在每个指定区间内元素的总和。

输入描述:
第一行输入为整数数组 Array 的长度 n，接下来 n 行，每行一个整数，表示数组的元素。随后的输入为需要计算总和的区间，直至文件结束。

输出描述:
输出每个指定区间内元素的总和。

输入示例
5
1
2
3
4
5
0 1
1 3
输出示例
3
9
数据范围：0 < n <= 100000
"""
import sys

 
def main():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]

    # 构建前缀和数组
    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + arr[i - 1]

    # 处理每个查询
    for line in sys.stdin:
        line = line.strip().split()
        left, right = int(line[0]), int(line[1])
        res = pre_sum[right + 1] - pre_sum[left]
        print(res)


if __name__ == "__main__":
    main()
