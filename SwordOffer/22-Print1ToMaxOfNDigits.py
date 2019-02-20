"""
打印从1到最大的n位数
题目：输入数字n，按顺序打印从1到最大的n位十进制数。
比如输入3，则打印出1、2、3一直到到最大的3位数999
注意：问题的全面性
当输入的n很大的时候，我们求最大的n位数是不是用整型（int）或者长整型（longlong）都会溢出？
即需要考虑大数问题。这是个陷阱，这里可以用字符串或者数组表达大数，下面用的是字符串
1. 在字符串表达的数字上模拟加法
2. 把字符串表达的数字打印出来
"""


class Solution:
    # 方法一：比较直观 模拟了整数的加法 代码有点长
    def Print1ToMaxNDigits(self, n):
        if n <= 0:
            return

        help = ['0'] * n
        # 如果没有溢出 则每次打印一个数
        while not self.increment(help):
            self.print_number(help)

    def increment(self, num_str):
        is_overflow = False         # 是否越界
        n_take_over = 0             # 是否进位
        str_len = len(num_str)
        # 这里写循环的目的是防止连续进位用的
        for i in range(str_len-1, -1, -1):
            n_sum = int(num_str[i]) + n_take_over
            # 只保证在最低位加1，且只加一次
            if i == str_len - 1:
                n_sum += 1
            if n_sum >= 10:
                if i == 0:
                    is_overflow = True
                else:
                    n_sum -= 10
                    n_take_over = 1
                    num_str[i] = str(n_sum)
            else:
                # 一旦进位完成 就break
                num_str[i] = str(n_sum)
                break
        return is_overflow

    def print_number(self, num_str):
        is_beginning_0 = True
        str_len = len(num_str)
        for i in range(0, str_len):
            if is_beginning_0 and num_str[i] != '0':
                is_beginning_0 = False

            if not is_beginning_0:
                print(''.join(num_str[i:]))
                break

    # 方法二：把问题转换成数字排列的解法，递归让代码更简洁
    # n位所有十进制数其实就是n个从0到9的全排列，即我们把数字的每一位从0到9排列一遍
    # 就得到了所有的十进制数。只是在打印的时候，排在前面的0不打印出来罢了
    # 全排列用递归很容易，数字的每一位都可能是0~9中的一个数，然后设置下一位。
    # 递归结束的条件是我们已经设置了数字的最后一位
    def Print1ToMaxNDigits1(self, n):
        if n <= 0:
            return
        help = ['0'] * n
        for i in range(0, 10):
            help[0] = str(i)    # 先给最高位设置为i
            self.print1_to_max_of_n_digits_recursively(help, n, 0)

    def print1_to_max_of_n_digits_recursively(self, num_str, str_len, index):
        if index == str_len-1:
            self.print_number(num_str)
            return

        for i in range(0, 10):
            num_str[index+1] = str(i)
            self.print1_to_max_of_n_digits_recursively(num_str, str_len, index+1)


obj = Solution()
obj.Print1ToMaxNDigits1(4)