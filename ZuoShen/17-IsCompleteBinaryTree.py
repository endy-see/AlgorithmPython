"""
判断一棵树是否是完全二叉树
思路：若设二叉树的深度为h，除第h层外，其它各层(1~h-1)的节点数都达到最大个数，
第h层所有的节点都连续集中在最左边，这就是完全二叉树。
（除了最后一层之外的其他每一层都被完全填充，并且所有节点都保持向左对齐）
解法：判断一棵树是否为完全二叉树：
1）左无右有 -> False
2）左无右无 -> 激活判断：之后所有节点都应是叶节点
3）左有右无 -> 激活判断：之后所有节点都应是叶节点
4）左有右有 -> 不用处理
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_CBT(root):
    if not root:
        return False

    queue = deque()
    queue.append(root)
    flag = False            # 是否激活判断过程
    while queue:
        root = queue.popleft()
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        if not root.left and root.right:    # 左空右不空 必不为CBT
            return False

        if flag:                            # 若过程激活则判断节点是否为叶节点
            if root.left or root.right:     # 存在左右孩子的必不为叶节点
                return False

        if not root.right:
            flag = True
    return True

