"""
深度优先遍历和宽度优先遍历（不止二叉树，可能多叉树）
深度优先遍历：
1.利用栈实现
2.从源节点开始把节点按照深度放入栈中，然后弹出
3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
4.直到栈变空
宽度优先遍历：
1.利用队列实现
2.从源节点开始依次按宽度进队列，然后弹出
3.每弹出一个点，把该节点所有没有进过队列的邻接点放入队列
4.直到队列变空
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.nexts = []


from collections import deque


# 先序非递归遍历
def DFS(root):
    if not root:
        return

    stack = []
    hash_set = set()
    stack.append(root)
    hash_set.add(root)
    print(root.val)
    while stack:
        cur = stack.pop()
        for next in cur.nexts:
            if next not in hash_set:
                # 只要cur.next中还有未被遍历的节点，cur都要不断入栈、出栈
                stack.append(cur)
                stack.append(next)
                hash_set.add(next)
                print(next.val)
                break


def BFS(root):
    if not root:
        return

    queue = deque()
    hash_set = set()
    queue.append(root)
    hash_set.add(root)
    while queue:
        cur = queue.popleft()
        print(cur.val)
        for next in cur.nexts:
            if next not in hash_set:
                hash_set.add(next)
                queue.append(next)


if __name__ == '__main__':
    root = Node(1)
    node2 = Node(4)
    node3 = Node(5)
    root.nexts = [Node(2), node2, Node(3), node3]
    node2.nexts = [Node(6), Node(7)]
    node3.nexts = [Node(8), Node(9), Node(10)]
    # DFS(root)
    BFS(root)