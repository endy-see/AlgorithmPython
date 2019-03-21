"""
判断一棵树是否是搜索二叉树
思路：若它左子树不空，则左子树上所有节点的值均小于它的根节点的值；
若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
它的左、右子树也分别为二叉排序树。（即中序遍历情况下，值一次增大）
"""

import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 二叉树的非递归遍历（把每次遍历到的节点都放入栈中来比较）
def is_bst(root):
    if not root:
        return False

    pre = -sys.maxsize
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if root.val < pre:
                return False
            else:
                pre = root.val
            root = root.right
    return True


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(14)
    print(is_bst(root))
