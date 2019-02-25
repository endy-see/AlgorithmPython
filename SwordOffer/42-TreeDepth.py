"""
二叉树的深度
题目：输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，
最长路径的长度为数的深度
思路：先序遍历
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        n_left = self.TreeDepth(pRoot.left)
        n_right = self.TreeDepth(pRoot.right)
        if n_left > n_right:
            return n_left + 1
        else:
            return n_right + 1


obj = Solution()
root = TreeNode(1)
tn1 = TreeNode(2)
tn2 = TreeNode(3)
root.left = tn1
root.right = tn2
tn3 = TreeNode(4)
tn4 = TreeNode(5)
tn1.left = tn3
tn1.right = tn4
tn5 = TreeNode(6)
tn2.right = tn5
tn6 = TreeNode(7)
tn4.left = tn6
print(obj.TreeDepth(root))