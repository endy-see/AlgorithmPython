"""
二叉搜索树与双向链表
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表
要求不能创建任何新的节点，只能调整树中节点指针的指向。
比如：     10
     6          14       ->   4->6->8->10->12->14->16
  4     8    12     16   ->   4<-6<-8<-10<-12<-14<-16

思路：二叉搜索树的中序遍历是单调递增的
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list_head = None
        self.list_tail = None

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree

        self.Convert(pRootOfTree.left)
        if not self.list_head:
            self.list_head = pRootOfTree
            self.list_tail = pRootOfTree
        else:
            self.list_tail.right = pRootOfTree
            pRootOfTree.left = self.list_tail
            self.list_tail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.list_head


obj = Solution()
root = TreeNode(10)
tn1 = TreeNode(6)
tn2 = TreeNode(14)
root.left = tn1
root.right = tn2
tn3 = TreeNode(4)
tn4 = TreeNode(8)
tn1.left = tn3
tn1.right = tn4
tn5 = TreeNode(12)
tn6 = TreeNode(16)
tn2.left = tn5
tn2.right = tn6
print(obj.Convert(root))

