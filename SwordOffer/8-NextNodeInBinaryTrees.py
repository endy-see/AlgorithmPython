
"""
二叉树的下一个节点
题目描述：
给定一课二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？
树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针
"""

"""
分析：
如果一个节点有右子树，那么它的下一个节点就是它的右子树中的最左子节点。即
从右子树出发一直沿着指向左子节点的指针，就能找到它的下一个节点。
如果一个节点没有右子树，那么就看当前节点与其父节点的关系：
如果当前节点是其父节点的左子孩子，那么它的下一个节点就是它的父节点
如果当前节点是其父节点的右子孩子，那么它的下一个节点就需要迭代往上找，直到找到
第一个是他父节点的左孩子的节点。如果这样的节点存在，那么此节点的父节点就是
要找的下一个节点；否则，遍历结束
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def getNext(self, cur_node):
        if not cur_node:
            return None

        if cur_node.right:
            next_node = cur_node.right
            while next_node.left:
                next_node = next_node.left
            return next_node
        elif cur_node.parent:
            parent_node = cur_node.parent
            if parent_node.left == cur_node:
                return parent_node
            else:
                cur_node = parent_node
                parent_node = parent_node.parent
                while parent_node and parent_node.left != cur_node:
                    cur_node = parent_node
                    parent_node = parent_node.parent
                return parent_node
        return None


obj = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node1.left = node2
node1.right = node3
node1.parent = None

node2.left = None
node2.right = None
node2.parent = node1

node3.left = node4
node3.right = node5
node3.parent = node1

node4.left = node6
node4.right = node7
node4.parent = node3

node5.left = None
node5.right = None
node5.parent = node3

node6.left = None
node6.right = None
node6.parent = node4

node7.left = node8
node7.right = None
node7.parent = node4

node8.left = None
node8.right = None
node8.parent = node7

print(obj.getNext(None))
print(obj.getNext(node5))


