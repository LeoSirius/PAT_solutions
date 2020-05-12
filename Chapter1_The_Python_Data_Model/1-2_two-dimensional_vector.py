

# __repr__() 会在终端、调试器和%r时被调用
# __str__() 会在print时被调用。
# 如果没有实现__str__()，解释器会调用__repr__()作为fallback

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # python用bool(obj)来取一个对象的布尔值
    # 一般来讲，一个自定义类对象的值是True，除非实现__bool__()或__len__()
    # bool(x)会先调用__bool__()，如果没有__bool__()，则调用__len__()
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scaler):
        return Vector(self.x * scaler, self.y * scaler)

if __name__ == '__main__':
    v = Vector(3, 4)

    print(f'{abs(v)}\n{v*3}\n{v}')
    # 5.0
    # Vector(9, 12)
    # Vector(3, 4)