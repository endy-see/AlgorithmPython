"""
机器人的运动范围
题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下
四个方向移动一个，但是不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够
进入方格（35，37），因为3+5+3+7=18.但是，它不能进入方格（35，38），因为3+5+3+8=19.
请问该机器人能够达到多少个格子？
思想：回溯法
"""


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 0 or cols < 0 or threshold < 0:
            return 0
        # 构造一个布尔类型的矩阵
        has_moved = [False] * rows
        for i in range(0, rows):
            has_moved[i] = [False] * cols
        self.moving_count(has_moved, rows, cols, 0, 0, threshold)
        res = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if has_moved[i][j]:
                    res += 1
        return res

    def moving_count(self, has_moved_matrix, rows, cols, row, col, threshold):
        if 0 <= row < rows and 0 <= col < cols and not has_moved_matrix[row][col] and \
                self.pos_digit_sum(row) + self.pos_digit_sum(col) <= threshold:
            has_moved_matrix[row][col] = True
            self.moving_count(has_moved_matrix, rows, cols, row + 1, col, threshold)
            self.moving_count(has_moved_matrix, rows, cols, row - 1, col, threshold)
            self.moving_count(has_moved_matrix, rows, cols, row, col + 1, threshold)
            self.moving_count(has_moved_matrix, rows, cols, row, col - 1, threshold)

    def pos_digit_sum(self, pos):
        pos_sum = 0
        while pos:
            pos_sum += pos % 10
            pos //= 10
        return pos_sum


obj = Solution()
print(obj.movingCount(18, 35, 37))
