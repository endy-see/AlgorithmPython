"""
题目：把数字人民币金额转换成大写
思路：
1. 先将字符串以小数点为分割符，分割成整数部分和小数部分
2. 将整数部分从高位到低位每个4个字符分一组（字符串切割）拆分成[兆，亿，万，仟]三组字符串组成的List:['0000','0000','0000']
   ex: 60019000010.70整数部分拆分为：['600','1900','0010']
3. 把切割后的每位（千、百、十、个）分别转换成汉字（大写化），注意零的处理
4. 拼接各个部分，并加上对应单位（兆、亿、万、元）
5. 小数部分特殊处理一下（发现python中小数点后输入超过2位后会被截断，所以这里只做了两位小数的判断
 decimal_dic = {0: u'角', 1: u'分', 2: u'厘', 3: u'毫'}
"""


class Num2MoneyFormat:
    def __init__(self):
        # 这里的顺序是从小到大（因为高位可能没有，但是低位会有）
        self.small_unit_dict = {1: u'', 2: u'拾', 3: u'佰', 4: u'仟'}
        self.big_unit_dict = {1: u'元', 2: u'万', 3: u'亿', 4: u'兆'}
        self.digit_dict = {'0': u'零', '1': u'壹', '2': u'贰', '3': u'叁', '4': u'肆',
                           '5': u'伍', '6': u'陆', '7': u'柒', '8': u'捌', '9': u'玖'}

    def num_to_money(self, data):
        split_data = str(data).split('.')

        integer_part = split_data[0]
        decimal_part = ''
        if len(split_data) > 1:
            decimal_part = split_data[1]
        i = 0
        res = u''
        # 分解字符数组[亿，万，仟]三组List:['0000','0000','0000']
        splited_integer_part = self.src_split(integer_part)
        # 获取拆分后的List长度
        splited_integer_part_len = len(splited_integer_part)

        # 大写合并
        for i in range(splited_integer_part_len):
            # 从高位往低位转（有可能一个字符串全是0的情况 这种情况不拼接）
            integer_str = self.convert_splited_integer_part(splited_integer_part[i])
            if integer_str:
                # 合并：前字符串大写+当前字符串大写+标识符
                res += integer_str + self.big_unit_dict[splited_integer_part_len - i]
        # 处理小数部分
        if decimal_part:
            decimal_part_len = len(decimal_part)
            if decimal_part_len == 1:  # 若小数只有1位
                if decimal_part[0] == '0':
                    res += u'整'
                else:
                    res += self.digit_dict[decimal_part[0]] + u'角'
            else:
                # 若小数有两位的四种情况
                if decimal_part[0] == '0' and decimal_part[1] == '0':
                    res += u'整'
                elif decimal_part[0] == '0' and decimal_part[1] != '0':
                    res += u'零' + self.digit_dict[decimal_part[1]] + u'分'
                elif decimal_part[0] != '0' and decimal_part[1] == '0':
                    res += self.digit_dict[decimal_part[0]] + u'角'
                else:
                    res += self.digit_dict[decimal_part[0]] + u'角' \
                          + self.digit_dict[decimal_part[1]] + u'分'
        return res

    # 拆分函数，将整数字符串拆分成[亿，万，仟]的list
    def src_split(self, integer_part):
        extra = len(integer_part) % 4
        res = []
        if extra > 0:
            res.append(integer_part[0:extra])

        index = extra
        while index < len(integer_part) - 1:
            res.append(integer_part[index:index + 4])
            index += 4
        return res

    # 对[亿，万，仟]的list中每个字符串分组进行大写化再合并
    def convert_splited_integer_part(self, mini_integer_part):
        mini_part_len = len(mini_integer_part)
        small_unit_key = mini_part_len
        res = u''
        for i in range(mini_part_len):
            # 某一位为0时
            if mini_integer_part[i] == '0':
                # 当前字符为'0'，而其下一个位置不为零时，要加上'零'字符
                if i < mini_part_len - 1 and mini_integer_part[i + 1] != '0':
                    res += self.digit_dict[mini_integer_part[i]]
            else:
                # 当前字符不为'0'，则形成格式为：数字+对应单位 的数据
                res += self.digit_dict[mini_integer_part[i]] + self.small_unit_dict[small_unit_key]
            small_unit_key -= 1
        return res


if __name__ == '__main__':
    pt = Num2MoneyFormat()
    # print(pt.num_to_money('600190101000.80'))
    print(pt.num_to_money(float('10001000000001.12')))
    # print(pt.num_to_money(1000200709.456))
    # digital_to_chinese(123456789.456)
