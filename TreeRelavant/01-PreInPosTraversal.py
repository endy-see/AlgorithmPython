"""
二叉树的先序、中序和后序遍历，递归和非递归方式
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pre_order_recur(self, root):
        if not root:
            return
        print(str(root.val))
        self.pre_order_recur(root.left)
        self.pre_order_recur(root.right)

    def in_order_recur(self, root):
        if not root:
            return
        self.in_order_recur(root.left)
        print(str(root.val))
        self.in_order_recur(root.right)

    def pos_order_recur(self, root):
        if not root:
            return
        self.pos_order_recur(root.left)
        self.pos_order_recur(root.right)
        print(str(root.val))

    def pre_order_unrecur(self, root):
        if root:
            stack = []
            stack.append(root)
            while stack:
                root = stack.pop()
                print(str(root.val) + ' ')
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

    def in_order_unrecur(self, root):
        if root:
            stack = []
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    print(root.val)
                    root = root.right

    # 是先序非递归的逆过程
    def pos_order_unrecur(self, head):
        if head:
            s1 = []
            s2 = []
            s1.append(head)
            while s1:
                head = s1.pop()
                s2.append(head)
                if head.left:
                    s1.append(head.left)
                if head.right:
                    s1.append(head.right)
            while s2:
                print(s2.pop().val)


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
# obj.pre_order_recur(root)
# obj.pre_order_unrecur(root)
# obj.in_order_recur(root)
# obj.in_order_unrecur(root)
# obj.pos_order_recur(root)
obj.pos_order_unrecur(root)

