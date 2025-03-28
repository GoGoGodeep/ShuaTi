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

n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

# 前缀和数组，第一个为0，便于计算
pre = [0] * (n + 1)

for i in range(n):
    pre[i+1] = pre[i] + nums[i]

for line in sys.stdin:
    line = list(line.strip().split())

    left, right = int(line[0]), int(line[1])
    print(pre[right+1] - pre[left])
