"""
最小路径和
题目：从左上角开始，只能向右或向下移动，求到右下角时时的最小路径和
"""


def min_path1(m):
    if not m or len(m) == 0 or not m[0] or len(m[0]) == 0:
        return 0
    return process1(m, len(m) - 1, len(m[0]) - 1)


# 递归版
def process1(m, i, j):
    res = m[i][j]
    if i == 0 and j == 0:
        return res
    if i == 0 and j != 0:
        return res + process1(m, i, j - 1)
    if i != 0 and j == 0:
        return res + process1(m, i - 1, j)
    return res + min(process1(m, i, j - 1), process1(m, i - 1, j))


# 动态规划版
def min_path2(m):
    if not m or len(m) == 0 or not m[0] or len(m[0]) == 0:
        return 0

    row = len(m)
    col = len(m[0])
    dp = [[0] * col for i in range(row)]
    dp[0][0] = m[0][0]
    for i in range(1, row):
        dp[i][0] = dp[i - 1][0] + m[i][0]
    for j in range(1, col):
        dp[0][j] = dp[0][j - 1] + m[0][j]
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]

    return dp[row - 1][col - 1]


m = [[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]
print(min_path1(m))
print(min_path2(m))
