"""
判断一个链表是否为回文结构
题目：给定一个链表的头节点head，请判断该链表是否为回文结构
例如: 1->2->1，返回true。 1->2->2->1，返回true。 15->6->15，返回true。 1->2->3，返回false。

进阶: 如果链表长度为N，时间复杂度达到O(N)，额外空间复杂 度达到O(1)。
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


# need n extra space
def isPalindrome1(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur)
        cur = cur.next

    while head:
        if head.value != stack.pop().value:
            return False
        head = head.value

    return True


# need n/2 extra space
def isPalindrome2(head):
    if not head or not head.next:
        return True

    # 让slow定位在链表的一半的下半部分（后半部分的回文）
    slow = head.next
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    stack = []
    while slow:
        stack.push(slow)
        slow = slow.next

    while stack:
        if head.value != stack.pop().value:
            return False
        head = head.next
    return True


# need O(1) extra space
def isPalindrome3(head):
    if not head or not head.next:
        return True

    n1 = head
    n2 = head
    # find mid node
    while n2.next and n2.next.next:
        n1 = n1.next  # n1->mid(上半部)
        n2 = n2.next.next  # n2->end

    # 把后半部分翻转 比较 最后再把后半部分转回来
    n2 = n1.next  # n2->right part first node
    n1.next = None  # mid.next->null
    while n2:  # right part convert
        n3 = n2.next  # save next node
        n2.next = n1  # next of right node convert
        n1 = n2  # n1 move
        n2 = n3  # n2 move

    n3 = n1  # save last node
    n2 = head  # left first node
    res = True
    while n1 and n2:
        if n1.value != n2.value:
            res = False
            break
        n1 = n1.next  # left to mid
        n2 = n2.next  # right to mid
    # 此时n3是后半部分的头部 n1和n2都指向了None
    n1 = n3.next
    n3.next = None
    # 让n1指向n3的下一个节点
    while n1:
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2
    return res


def print_linked_list(head):
    print('Linked List:')
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    # print_linked_list(head)
    print(isPalindrome3(head))
