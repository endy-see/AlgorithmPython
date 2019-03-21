"""
换钱的方法数
题目：给定数组arr，arr中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币
可以使用任意张，再给定一个整数aim代表要找的钱数，求换钱有多少种方法
"""


def money1(arr, aim):
    return process1(arr, 0, 0, aim)


def process1(arr, i, sum, aim):
    if sum == aim:
        return True
    if i == len(arr):
        return False
    return process1(arr, i+1, sum, aim) or process1(arr, i+1, sum+arr[i], aim)


def money2(arr, aim):
    dp = [[False]*(aim+1) for i in range(len(arr)+1)]
    for i in range(len(dp)):
        dp[i][aim] = True
    for i in range(len(arr)-1, -1, -1):
        for j in range(aim-1, -1, -1):
            dp[i][j] = dp[i+1][j]
            if j + arr[i] <= aim:
                dp[i][j] = dp[i][j] or dp[i+1][j+arr[i]]
    return dp[0][0]


arr = [1, 4, 8]
aim = 12
print(money1(arr, aim))
print(money2(arr, aim))