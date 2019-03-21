"""
Knapsack背包问题
题目：给定n个items的weights和values，把这些items放到一个容量为W的背包里来获取背包内items的最大的总value值
换句话说，给定两个整数数组val[0..n-1]和wt[0..n-1]分别代表n个items的values和weights
还给定了一个整数W表示背包的容量，找出val[]子集的最大值（同时这个子集的weights和要小于等于W）
思路：递归和非递归算法 时间复杂度O(n*W)
"""

import sys


def max_value1(c, p, bag):
    return process1(c, p, 0, 0, bag)


def process1(c, p, i, cost, bag):
    if cost > bag:
        return -sys.maxsize
    if i == len(c):
        return 0
    return max(process1(c, p, i + 1, cost, bag),
               p[i] + process1(c, p, i + 1, cost + c[i], bag))


def max_value2(c, p, bag):
    dp = [[0]*(bag+1) for i in range(len(c)+1)]
    for i in range(len(c) - 1, -1, -1):
        for j in range(bag, -1, -1):
            dp[i][j] = dp[i + 1][j]
            if j + c[i] <= bag:
                dp[i][j] = max(dp[i][j], p[i] + dp[i + 1][j + c[i]])

    return dp[0][0]


c = [3, 2, 4, 7]
p = [5, 6, 3, 19]
bag = 11
print(max_value1(c, p, bag))
print(max_value2(c, p, bag))

