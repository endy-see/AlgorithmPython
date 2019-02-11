# 题目描述
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, mid):
        # write code here
        if not pre or not mid or len(pre) < 1 or len(mid) < 1 or len(pre) != len(mid):
            return None

        # 前序遍历的第一个节点一定是根节点
        root_value = pre[0]
        for i in range(0, len(mid)):
            if mid[i] == root_value:
                break
        # 递归构造左子树和右子树
        left = self.reConstructBinaryTree(pre[1:1 + i], mid[:i])
        right = self.reConstructBinaryTree(pre[i + 1:], mid[i + 1:])

        root = TreeNode(root_value)
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
    obj = Solution()
    root = obj.reConstructBinaryTree(pre_order, mid_order)
    print(root.val)
