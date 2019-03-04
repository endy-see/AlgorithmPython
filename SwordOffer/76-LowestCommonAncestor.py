"""
树中两个节点的最低公共祖先节点
题目：输入两个树节点，求它们的最低公共祖先节点
注意：与面试官的交流
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 这棵树是否是二叉树 -> 是二叉树，且是二叉搜索树
# 二叉搜索树是经过排序的，位于左子树的节点都比父节点小，位于右子树的节点都比父节点大。既然要找最低的公共祖先节点，我们可以从根节点开始进行比较。
# 若当前节点的值比两个节点的值都大，那么最低的祖先节点一定在当前节点的左子树中，则遍历当前节点的左子节点；
# 反之，若当前节点的值比两个节点的值都小，那么最低的祖先节点一定在当前节点的右子树中，则遍历当前节点的右子节点；
# 这样，直到找到一个节点，位于两个节点值的中间，则找到了最低的公共祖先节点。
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# 如果是普通的二叉树呢？ -> 树的节点中有没有指向父节点的指针？
# 如果存在parent指针，则分别从输入的p节点和q节点指向root根节点，其实这就是两个单链表。
# 问题转化为求两个单链表相交的第一个公共节点...

# 那如果不存在parent指针呢？
# 递归的解法如下：
class Solution1:
    def lowestCommonAncestor1(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


# 迭代解法
# 需要我们保存下由root根节点到p和q节点的路径，并且将路径存入list中，
# 则问题转化为求两个list集合的最后一个共同元素。
class Solution2:
    def lowestCommonAncestor2(self, root, p, q):
        if not root or root == p or root == q:
            return root
        pathp = []
        pathq = []
        pathp.append(root)
        pathq.append(root)

        self.get_path(root, p, pathp)
        self.get_path(root, q, pathq)

        res = None
        i = 0
        while i < len(pathp) and i < len(pathq):
            if pathp[i] == pathq[i]:
                res= pathp[i]
            else:
                break
        return res

    def get_path(self, root, n, path):
        if root == n:
            return True
        if root.left:
            path.append(root.left)
            if self.get_path(root.left, n, path):
                return True
            path.remove(path[-1])

        if root.right:
            path.append(root.right)
            if self.get_path(root.right, n, path):
                return True
            path.remove(path[-1])

        return False