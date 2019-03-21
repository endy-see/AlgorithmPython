"""
KMP算法扩展二：
给定两个二叉树T1和T2，返回T1的某个子树结构是否与T2的结构相等
思路：
1. 分别先对t1和t2做相同的序列化操作（前序遍历），得到s1和s2
2. 用KMP在s1中找s2第一次出现的位置，如果有，就说明t2是t1的子树
"""


class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def is_subtree(t1, t2):
    s1 = serial_by_pre(t1)
    s2 = serial_by_pre(t2)
    return get_index_of(s1, s2) != -1


def serial_by_pre(root):
    if not root:
        return '#_'

    res = str(root.value) + '_'
    res += serial_by_pre(root.left)
    res += serial_by_pre(root.right)
    return res


# 用KMP算法，在s1中找到s2第一次出现的位置
def get_index_of(s1, s2):
    if not s1 and s2:
        return -1

    next = get_next_array(s2)
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif next[j] == -1:
            i += 1
        else:
            j = next[j]
    return i-j if j == len(s2) else -1


def get_next_array(s):
    if not s or len(s) <= 1:
        return [-1]

    next = [0] * len(s)
    next[0] = -1
    next[1] = 0
    cn = 0
    pos = 2

    while pos < len(s):
        if s[pos - 1] == s[cn]:
            next[pos] = cn + 1
            pos += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1
    return next


if __name__ == '__main__':
    root = Node(1)
    n1 = Node(2)
    n2 = Node(3)
    root.left = n1
    root.right = n2
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(6)
    n6 = Node(7)
    n7 = Node(8)
    n8 = Node(9)
    n1.left = n3
    n1.right = n4
    n3.right = n7
    n4.left = n8
    n2.left = n5
    n2.right = n6

    root2 = Node(2)
    root2.left = Node(4)
    root2.right = Node(5)
    root2.left.right = Node(8)
    root2.right.left = Node(9)

    print(is_subtree(root, root2))