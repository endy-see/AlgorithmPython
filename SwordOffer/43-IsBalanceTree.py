"""
平衡二叉树
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
如果某二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是一颗平衡二叉树
例如：下图就是一颗平衡二叉树
        1
    2       3
  4   5        6
    7
思路：后序遍历 先分别判断左右子树是否平衡，然后再根据左右子树的深度，综合判断当前节点否平衡
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True

        is_left_balance = self.IsBalanced_Solution(pRoot.left)
        is_right_balance = self.IsBalanced_Solution(pRoot.right)

        n_left = self.get_cur_node_depth(pRoot.left)
        n_right = self.get_cur_node_depth(pRoot.right)

        return is_left_balance and is_right_balance and abs(n_left - n_right) < 2

    def get_cur_node_depth(self, root):
        if not root:
            return 0
        n_left = self.get_cur_node_depth(root.left)
        n_right = self.get_cur_node_depth(root.right)
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
print(obj.IsBalanced_Solution(root))