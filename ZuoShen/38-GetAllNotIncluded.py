"""
题目：一个数组长度为N，包含n个元素，另一个数组长度M，包含m个元素
要求找到M中不在N中的元素（两个数组均无序）
方法1.暴力求解
     将M中的元素去N中遍历，有则打印，没有则继续
     时间复杂度O(M*N)
方法2.二分查找
1）将N中的元素进行排序，假设时间复杂度O(A)
2) N有序
3）M中的元素到N中去二分查找
时间复杂度O(A)+O(M*logN)，然后二者取最大即可
"""


def GetAllNotIncluded(A, B):
    A.sort()
    res = []
    for i in range(len(B)):
        l = 0
        r = len(A)-1
        contains = False
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == B[i]:
                contains = True
                break
            if A[mid] > B[i]:
                r = mid - 1
            else:
                l = mid + 1
        if not contains:
            res.append(B[i])
    return res


A = [4, 2, 5, 6]
B = [7, 2, 5, 8]
print(GetAllNotIncluded(A, B))


