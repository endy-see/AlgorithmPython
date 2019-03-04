"""
数字序列中某一位的数字
题目：数字以0123456789101112131415...的格式序列化到一个字符序列中。在这个序列中，
第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一个函数，求任意第n位对应的数字
思路：
1.从0开始逐一枚举每个数字。每枚举一个数字的时候，获取当前数字的位置，如果当前的位置就是目标位置，则直接返回
2. 找规律（推荐）
  1）在循环中，不断用integer_nums_of_weishu找每个位数对应的所有数字的个数numbers
  ex: 一位数对应的数字范围：0~9，有10个；两位数对应的数字范围10~99，共90个
  然后numbers*wei_shu表示截止到当前整数数字为止（如99），当前wei_shu的所有数字的所有字符的个数
  2）如果index < numbers*wei_shu，说明目标index已经包含在了当前wei_shu；然后用digit_at_index方法精确定位
  否则不断用numbers*wei_shu去抵消index，这样只需要在后续遍历到某一位时，直接确定当前的index位置上的数就可以了
  3)精确定位digit_at_index：首先获取index所在的数字：number = begin_number_of_weishu(digits) + index // digits
    最后在number的余数位的数字number[index//digits]就是结果了，但是由于是数字，所以取对应位的数字需要不断取整、取余的运算
  ex: 811 < 2700，所以第811位是某个三位数中的一位。由于811=270*3+1，即第811位是从100
      开始的第270个数字，即370的中间一位，也就是7
"""


# 方法一
def digitAtIndext1(num_str, index):
    for pos, val in enumerate(num_str):
        if pos == index:
            return val
    return None


# 推荐：方法二
def digitAtIndex(index):
    if index < 0:
        return -1
    wei_shu = 1
    while True:
        numbers = integer_nums_of_weishu(wei_shu)
        if index < numbers * wei_shu:
            return digit_at_index(index, wei_shu)
        index -= wei_shu * numbers
        wei_shu += 1
    return -1


# 得到m位的数字总共有多少个
# ex：输入2，则返回两位数（10-99）的个数90；
# 输入3，则返回三位数（100-999）的个数900
def integer_nums_of_weishu(wei_shu):
    if wei_shu == 1:
        return 10
    count = int(pow(10, wei_shu - 1))
    return 9 * count


# 当我们知道要找的那一位数字位于某m位数之后，就可以用如下函数找出那一位数字
def digit_at_index(index, wei_shu):
    # number是在所有wei_shu的数字中index位所在的数字具体
    number = begin_number_of_weishu(wei_shu) + index // wei_shu
    tmp = index % wei_shu
    # 结果就是number的第index%wei_shu+1位的数字
    # 下面是为了从数字中取到这一位的逻辑：从number右边开始不断对num取整，最后返回对num取余即可
    index_from_right = wei_shu - index % wei_shu
    for i in range(1, index_from_right):
        number //= 10
    res = number % 10
    return res


# 返回m位数字的第一个数字
# ex：第一个两位数是10，第一个三位数是100，第一个4位数是1000
def begin_number_of_weishu(digits):
    if digits == 1:
        return 0
    return int(pow(10, digits - 1))


# print(digitAtIndext1('0123456789101112131415', 5))
# print(digitAtIndext1('0123456789101112131415', 13))
print(digitAtIndex(1012))
