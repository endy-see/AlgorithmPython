"""
对称二叉树
题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，在下图所示的4棵二叉树中，第一颗二叉树是对称的，领另外两棵不是
        8                       8                       7
    6       6               6       9               7       7
 5     7  7    5          5   7   7   5           7   7   7
思路：
通常有3种二叉树的遍历算法：前序、中序和后序。这3种遍历都是先遍历左孩子再遍历右孩子
这里我们定义一种遍历算法，先遍历右孩子再遍历做孩子。
先序遍历root1和自定义序遍历root2，遇到None时，只有root1和root2
都为None时才返回True，其中只有一个None时返回False
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.is_symmetrical(pRoot, pRoot)

    def is_symmetrical(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False

        return self.is_symmetrical(root1.left, root2.right) \
               & self.is_symmetrical(root1.right, root2.left)


obj = Solution()
root = TreeNode(8)
tn1 = TreeNode(6)
tn2 = TreeNode(9)
root.left = tn1
root.right = tn2
tn3 = TreeNode(5)
tn4 = TreeNode(7)
tn1.left = tn3
tn1.right = tn4
tn5 = TreeNode(7)
tn6 = TreeNode(5)
tn2.left = tn5
tn2.right = tn6
print(obj.isSymmetrical(root))

