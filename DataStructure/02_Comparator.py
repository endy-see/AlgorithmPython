"""
python的比较器
对比较运算符重载
lt:  小于
le：　小于等于
gt：　大于
ge：　大于等于
eq：　等于
ne：　不等于
为了比较不同对象，将不同对象都继承一个类，在类中给出一个抽象函数
让需要参与的比较对象实现
"""


class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()


rect1 = Rectangle(1.0, 2.0)
rect2 = Rectangle(1.0, 2.0)
print(rect1 != rect2)
