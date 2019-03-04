"""
礼物的最大价值
题目：在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或向下移动一格，直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
ex:
1   10  3   8
12  2   9   6
5   7   4   11
3   7   16  5
思路：典型的动态规划问题，先用递归的思路来分析。
1. 定义f(i,j)表示到达(i,j)格子时能拿到的礼物总和的最大值，根据题目要求，有两种可能的途径到达
坐标为(i,j)的格子：通过格子(i-1,j)或者(i,j-1)。所以f(i,j)=max(f(i-1,j),f(i,j-1))+gift[i,j]
gift[i,j]表示坐标为(i,j)的格子里礼物的价值
2. 尽管用递归分析问题，但是由于有大量的重复计算，导致递归的代码并不是最优的。相对而言，基于循环的
代码效率要高很多。为了缓存中间的计算结果，需要一个辅助的二维数组。数组中坐标为(i,j)的元素表示
到达坐标为(i,j)的格子时能够拿到的礼物价值总和的最大值
方法一：空间复杂度O(M*N)，需要一个二维的dp矩阵，先把第一行和第一列赋值，然后循环算dp[i][j]的值
方法二：空间复杂度O(min{M,N}) 根据给定矩阵行和列的大小关系，决定滚动的方式，始终生成最小长度(min{M,N})的dp数组
二者时间复杂度均O(M*N)
"""


# 方法一：O(M*N)
def MaxGiftValue(matrix):
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*cols for i in range(rows)]
    dp[0][0] = matrix[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[rows-1][cols-1]


# 方法二：O(min(M,N))
def MaxGiftValue1(matrix):
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return 0

    # 行与列数较大的那一个
    more = max(len(matrix), len(matrix[0]))
    # 行与列数较小的那一个
    less = min(len(matrix), len(matrix[0]))
    # 行数是不是大于列数
    rowmore = more == len(matrix)
    dp = [0]*less
    dp[0] = matrix[0][0]
    # 给dp赋初值
    for i in range(1, less):
        if rowmore:
            dp[i] = dp[i-1] + matrix[0][i]
        else:
            dp[i] = dp[i-1] + matrix[i][0]
    for i in range(1, more):
        if rowmore:
            dp[0] += matrix[i][0]
        else:
            dp[0] += matrix[0][i]
        for j in range(1, less):
            if rowmore:
                dp[j] = max(dp[j-1], dp[j]) + matrix[i][j]
            else:
                dp[j] = max(dp[j-1], dp[j]) + matrix[j][i]
    return dp[less-1]


matrix = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
print(MaxGiftValue1(matrix))
