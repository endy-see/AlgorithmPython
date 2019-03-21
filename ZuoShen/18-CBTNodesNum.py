"""
给出一棵完全二叉树，求出该树的节点个数
要求：时间复杂度低于O(N)，N为这棵树的节点个数
完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
方法一：递归
方法二：迭代
    二叉树的性质（n从0开始）：
    1）二叉树的第n层最多为2^n个节点
    2）二叉树最多有2^(n+1)-1个节点（满二叉树）
思路：如果右子树的高度等于整棵二叉树的高度-1的话，那么右子树是满的，继续对左子树的左右子树高度做比较

"""


def count_nodes1(root):
    if not root:
        return 0
    if root.left and root.right:
        return count_nodes1(root.left) + count_nodes1(root.right)
    if root.right:
        return count_nodes1(root.right) + 1
    if root.left:
        return count_nodes1(root.left) + 1


# 如果将None也看做是一个二叉树的话，那么问题变得容易（只存在root空或非空）
def count_nodes2(root):
    return count_nodes2(root.left) + count_nodes2(root.right) + 1 if root else 0


# 获取左子树的高度
def get_left_height(root):
    count = 0
    while root:
        count += 1
        root = root.left
    return count


def get_right_height(root):
    count = 0
    while root:
        count += 1
        root.root.right
    return count


def count_nodes3(root):
    if not root:
        return 0
    left_height = get_left_height(root)
    right_height = get_right_height(root)
    if left_height == right_height:
        # 满二叉树，二叉树的节点数直接由公式2^(n-1)得到
        # 注：1 << left_height使用位运算计算2^left_height效率更高
        return (1 << left_height) - 1
    else:
        # 若该二叉树不是满二叉树，递归的调用该方法，计算左子树和右子树的节点数
        return count_nodes3(root.left) + count_nodes3(root.right)+1
