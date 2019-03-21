"""
字符串中字符的全排列
"""


def printAllPermutation(s):
    if not s or len(s) < 1:
        return
    process1(list(s), 0)


def process1(chs, i):
    if i == len(chs):
        print(''.join(chs))
    for j in range(i, len(chs)):
        swap(chs, i, j)
        process1(chs, i + 1)
        swap(chs, i, j)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


printAllPermutation('abc')


