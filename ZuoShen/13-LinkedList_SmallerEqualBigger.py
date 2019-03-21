"""
链表的partition: 将单链表按某值划分成左边小、中间相等、右边大的形式
题目：给定一个单向链表的头节点head，节点的值类型是整型，再给定一个整数pivot。
实现一个调整链表的函数，将链表调整为左部分都是值小于pivot的节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点
除这个要求外，对调整后的节点顺序没有更多的要求。例如：
链表9->0->4->5->1，pivot=3。调整后链表可以是1->0->4->9->5，也可以是0->1->9->5->4。
总之，满足左部分都是小于3的节点，中间部分都是等于3的节点(本例中这个部 分为空)，右部分都是大于3的节点即可。对某部分内部的节点顺序不做要求。

进阶: 在原问题的要求之上再增加如下两个要求。
在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左到右的顺序与原链表中节点的先后次序一致。
例如:链表9->0->4->5->1，pivot=3。 调整后的链表是0->1->9->4->5。
在满足原问题要求的同时，左部分节点从左到右为0、1。在原链表中也是先出现0，后出现1;中间部分在本例中为空，不再讨论;
右部分节点从左到右为9、4、5。在原链表中也是先出现9，然后出现4，最后出现5。
如果链表长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def list_Partition1(head, pivot):
    if not head:
        return head

    # 统计节点个数
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next

    node_arr = [None] * count
    cur = head
    for i in range(len(node_arr)):
        node_arr[i] = cur
        cur = cur.next

    partition(node_arr, pivot)

    for i in range(1, len(node_arr)):
        if i == len(node_arr)-1:
            node_arr[i].next = None
        node_arr[i-1].next = node_arr[i]
    return node_arr[0]


def partition(node_arr, pivot):
    small = -1
    big = len(node_arr)
    cur = 0
    while cur != big:
        if node_arr[cur].value < pivot:
            swap(node_arr, small+1, cur)
            small += 1
            cur += 1
        elif node_arr[cur].value > pivot:
            swap(node_arr, big-1, cur)
            big -= 1
        else:
            cur += 1


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def list_Partition2(head, pivot):
    sH = None  # small head
    sT = None  # small tail
    eH = None  # equal head
    eT = None  # equal tail
    bH = None  # big  head
    bT = None  # big tail
    # every node distributed to three lists
    while head:
        next = head.next
        head.next = None
        if head.value < pivot:
            if not sH:
                sH = head
                sT = head
            else:
                sT.next = head
                sT = head
        elif head.value < pivot:
            if not eH:
                eH = head
                eT = head
            else:
                eT.next = head
                eT = head
        else:
            if not bH:
                bH = head
                bT = head
            else:
                bT.next = head
                bT = head

        head = next

    # small and equal reconnect
    if sT:
        sT.next = eH
        if not eT:
            eT = sT

    # all reconnect
    if eT:
        eT.next = bH

    if sH:
        return sH
    elif eH:
        return eH
    else:
        return bH


if __name__ == '__main__':
    head = Node(9)
    head.next = Node(0)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)
    # res_head = list_Partition1(head, 3)
    res_head = list_Partition2(head, 3)
    print(res_head)

