"""
二叉树的镜像
题目：
操作给定的二叉树，将其变换为源二叉树的镜像
思路：求一棵树的镜像的过程如下：
先前序遍历这棵树的每个节点，如果遍历到的节点有子节点，就交换它的两个子节点
当交换完所有非叶节点的左、右子节点之后，就得到了树的镜像
"""


# _*_coding:utf-8_*_
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return root

        self.mirror(root)
        return root

    def mirror(self, root):
        if not root:
            return

        # root左右子树中有一个为空时也可以交换
        # 交换根节点的左右子树
        self.swap(root)
        self.mirror(root.left)
        self.mirror(root.right)

    def swap(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp

