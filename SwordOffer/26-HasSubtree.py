"""
数的子结构
题目：输入两棵二叉树A，B，判断B是不是A的子结构。(ps: 约定空树不是任意一个数的子结构)
思路：分两步
第一步：递归遍历树A，在树A中找到和树B的根节点的值一样的节点R
第二步：判断数A中以R为根节点的子树是不是包含和树B一样的结构
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.has_subtree(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def has_subtree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False

        return self.has_subtree(root1.left, root2.left) and \
               self.has_subtree(root1.right, root2.right)
