"""
顺时针打印矩阵
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵：
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
思路：卡主左上角点和右下角点
"""


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        tR = 0
        tC = 0
        dR = len(matrix) - 1
        dC = len(matrix[0]) - 1
        while tR <= dR and tC <= dC:
            self.print_edge(matrix, tR, tC, dR, dC, res)
            tR += 1
            tC += 1
            dR -= 1
            dC -= 1
        return res

    def print_edge(self, m, tR, tC, dR, dC, res):
        if tR == dR:
            for i in range(tC, dC + 1):
                res.append(m[tR][i])
                # print(str(m[tR][i]) + ',')
        elif tC == dC:
            for i in range(tR, dR + 1):
                res.append(m[i][tC])
                # print(str(m[i][tC]) + ',')
        else:
            curC = tC
            curR = tR
            while curC != dC:
                res.append(m[tR][curC])
                # print(str(m[tR][curC]) + ',')
                curC += 1
            while curR != dR:
                res.append(m[curR][dC])
                # print(str(m[curR][dC]) + ',')
                curR += 1
            while curC != tC:
                res.append(m[dR][curC])
                # print(str(m[dR][curC]) + ',')
                curC -= 1
            while curR != tR:
                # print(str(m[curR][tC]) + ',')
                res.append(m[curR][tC])
                curR -= 1


obj = Solution()
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix = [[1]]
print(obj.printMatrix(matrix))