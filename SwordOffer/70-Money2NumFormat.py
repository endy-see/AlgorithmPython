"""
中文(大写)数字转阿拉伯数字
题目：中文转数字，小数的化考虑点字进一步封装即可
思路：逆序分解 再逆序拼接
1. 逆序遍历每个字符
   1）如果当前字符是单位，则从单位字典中获取该单位对应的数值。另外还需判断当前的单位值是否是10000或100000000
   因为这两个单位是分界点，而千、百、十、个则是会重复的
   2）如果当前字符是数字，则从数字字典中获取该数字对应值。如果之前有单位保留，则当前值乘以该单位值作为结果的一部分，
   并将单位值重新归零；如果当前之前没有单位值（当前值为零，之前的值也是数字），就以当前值作为结果的一部分
   3）如果最后的unit=10，说明数字在11-19之间，需要特殊处理
2. 将结果数组中的每个值再逆序相加成数字
   1）如果遇到10000或100000000，则需要当前数（千百十）乘以这样的单位后再累加
   2）如果是千百十，则直接累加
ex:
十一, 一百, 一百二十三, 一万一千一百零一, 一亿一千一百二十三万四千五百六十七...
"""

# constants for chinese_to_arabic
digit_dict = {
    '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
    '零': 0, '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '两': 2,
}

unit_dict = {
    '十': 10,
    '拾': 10,
    '百': 100,
    '佰': 100,
    '千': 1000,
    '仟': 1000,
    '万': 10000,
    '萬': 10000,
    '亿': 100000000,
    '億': 100000000,
    '兆': 1000000000000,
}


def chinese_to_arabic(money_str):
    unit = 0
    res_digit = []
    for cur_char in reversed(money_str):
        if cur_char in unit_dict:
            unit = unit_dict.get(cur_char)
            if unit == 10000 or unit == 100000000:
                res_digit.append(unit)
                unit = 1
        else:
            digit = digit_dict.get(cur_char)
            if unit:
                digit *= unit
                unit = 0
            res_digit.append(digit)
    if unit == 10:
        res_digit.append(10)

    res, tmp = 0, 0
    for digit in reversed(res_digit):
        if digit == 10000 or digit == 100000000:
            res += tmp * digit
            tmp = 0
        else:
            tmp += digit
    res += tmp
    return res


# TODO: make a full unittest
def get_chinese_to_arabic():
    # test_dig = ['八',
    #             '十一',
    #             '一百二十三',
    #             '一千二百零三',
    #             '一万一千一百零一',
    #             '十万零三千六百零九',
    #             '一百二十三万四千五百六十七',
    #             '一千一百二十三万四千五百六十七',
    #             '一亿一千一百二十三万四千五百六十七',
    #             '一百零二亿五千零一万零一千零三十八']
    # test_dig = ['一百零二亿五千零一万零一千零三十八']
    # test_dig = ['一百零二亿五千零一万一千一百一十']
    test_dig = ['十一', '一百']
    for cn in test_dig:
        x = chinese_to_arabic(cn)
        print(cn, x)
    # assert x == 10250011038


if __name__ == '__main__':
    get_chinese_to_arabic()