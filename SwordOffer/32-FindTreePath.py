"""
二叉树中和为某一值的路径
题目：
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径
路径定义为从树的根节点开始往下一直到叶节点所经过的节点形成一条直线。
（注意：在返回值的list中，数组长度大的数组靠前）
思路：由于路径是从根节点出发到叶节点，所以首先需要遍历根节点->前序
每访问一个节点，就需要把当前节点添加到路径上，并累加该节点的值。
如果该节点为叶节点，并且路径中节点值的和刚好等于输入的整数，则当前路径符合要求
如果当前节点不是叶节点，则继续访问它的子节点。当前节点访问结束后，递归函数将
自动回到它的父节点。因此，在函数退出之前要在路径上删除当前节点并减去当前
节点的值，以确保返回父节点时路径刚好是从根节点到父节点。
不难看出，保存路径的数据结构实际上是一个栈，因为路径要与递归调用状态
一致，而递归调用的本质就是一个压栈和出栈的过程
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root:
            return res

        cur_sum = 0
        self.find_path(root, expectNumber, [], cur_sum, res)
        return res

    def find_path(self, root, expect_num, cur_path, cur_sum, res):
        cur_sum += root.val
        cur_path.append(root.val)

        is_leaf = root.left is None and root.right is None
        # 如果是叶节点，并且路径上节点值的和等于输入的值
        if is_leaf and cur_sum == expect_num:
            # 注意此处不能直接写res.append(cur_path),因为下面的pop会影响到res中存放的cur_path
            res.append(tuple(cur_path))
            # 注意此处不能return 因为加到res后还必须要pop当前栈顶

        # 如果不是叶节点，则遍历它的子节点
        if root.left:
            self.find_path(root.left, expect_num, cur_path, cur_sum, res)
        if root.right:
            self.find_path(root.right, expect_num, cur_path, cur_sum, res)

        # 在返回父节点之前，在路径上删除当前节点
        cur_path.pop()
        # 此处不用对cur_sum减 因为能走到这一步，就是当前root节点左右都遍历了，
        # 回到上层递归时cur_sum是未加root.val的位置


obj = Solution()
root = TreeNode(10)
tn1 = TreeNode(5)
tn2 = TreeNode(12)
tn3 = TreeNode(4)
tn4 = TreeNode(7)
root.left = tn1
root.right = tn2
tn1.left = tn3
tn1.right = tn4
print(obj.FindPath(root, 22))