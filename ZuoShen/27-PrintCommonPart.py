"""
打印两个有序链表的公共部分
题目: 给定两个有序链表的头指针head1和head2，打印两个 链表的公共部分。
"""


def printCommonPart(head1, head2):
    while head1 and head2:
        if head1.value < head2.value:
            head1 = head1.next
        elif head1.value > head2.value:
            head2 = head2.next
        else:
            print(head1.value)
            head1 = head1.next
            head2 = head2.next

