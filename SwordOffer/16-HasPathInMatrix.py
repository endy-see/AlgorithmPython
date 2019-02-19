"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如:  a b c e s f c s a d e e
a b c e
s f c s
a d e e
这样的3 X 4矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

思路：回溯法
"""


# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows < 0 or cols < 0 \
                or not path or len(path) < 1 \
                or len(path) > rows * cols:
            return False
        # 需要先构建一个和matrix相同大小的布尔矩阵
        visited = [False]*rows*cols

        for i in range(0, rows):
            for j in range(0, cols):
                # 先复制一个和matrix相同的矩阵
                if self.has_path(matrix, rows, cols, i, j, path, 0, visited):
                    return True
        return False

    def has_path(self, matrix, rows, cols, row, col, path, path_cur_index, visited):
        if path_cur_index == len(path):
            return True

        hasPath = False
        if 0 <= row < rows and 0 <= col < cols \
                and matrix[row * cols + col] == path[path_cur_index] \
                and not visited[row * cols + col]:
            path_cur_index += 1
            visited[row * cols + col] = True
            hasPath = self.has_path(matrix, rows, cols, row + 1, col, path, path_cur_index, visited) \
                      or self.has_path(matrix, rows, cols, row - 1, col, path, path_cur_index, visited) \
                      or self.has_path(matrix, rows, cols, row, col + 1, path, path_cur_index, visited) \
                      or self.has_path(matrix, rows, cols, row, col - 1, path, path_cur_index, visited)
            if not hasPath:
                path_cur_index -= 1
                visited[row*cols+col] = False
        return hasPath


obj = Solution()
matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']
print(obj.hasPath(matrix, 3, 4, 'bcced'))
