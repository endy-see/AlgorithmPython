"""
二叉搜索树的第k个节点
题目：给定一棵二叉搜索树，请找出其中第k大的节点。例如，在下图中的二叉搜索树中，
按节点数值大小顺序，第三大节点的值是4
        5
    3       7
  2   4   6   8
思路：二叉搜索树的中序遍历是非递减的，遍历到的第k个数就是结果
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.k = 0
        self.res = None
        self.count = 0

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k < 1:
            return None

        self.k = k
        self.kth_node(pRoot)
        return self.res

    def kth_node(self, root):
        if not root:
            return

        self.kth_node(root.left)
        self.count += 1
        # 这里只是保留下来了count==k时的节点 但是中序遍历还是会进行到底的
        if self.count == self.k:
            self.res = root
            return
        self.kth_node(root.right)


obj = Solution()
root = TreeNode(5)
tn1 = TreeNode(3)
tn2 = TreeNode(7)
root.left = tn1
root.right = tn2
tn3 = TreeNode(2)
tn4 = TreeNode(4)
tn1.left = tn3
tn1.right = tn4
tn5 = TreeNode(6)
tn6 = TreeNode(8)
tn2.left = tn5
tn2.right = tn6
print(obj.KthNode(root, 3).val)
