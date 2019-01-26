"""
给定一个字符串类型的数组strs，找到一种拼接方式，
使得把所有字符串拼起来之后形成的字符串具有最低的字典序
"""

import heapq

class node:
    def __init__(self, str_):
        self.str_ = str_

    def __lt__(self, other):
        return self.str_ + other.str_ < other.str_ + self.str_


def get_minist_lexicongraph(str_arr):
    if not str_arr:
        return []

    str_heap = []
    for i in range(len(str_arr)):
        heapq.heappush(str_heap, str_arr[i])

    return str_heap


if __name__ == '__main__':
    strs1 = ["jibw", "ji", "jp", "bw", "jibw" ]
    print(get_minist_lexicongraph(strs1))

    strs2 = ['ba', 'b']
    print(get_minist_lexicongraph(strs2))