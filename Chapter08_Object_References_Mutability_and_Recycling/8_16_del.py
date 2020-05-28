# del删除的是变量名，不是对象。
# __del__()则类似c++的析构函数，是删除对象前解释器调用的。调用完后，释放内存。

# CPython中GC采用引用计数的方法。对象没有引用，则被释放。

import weakref

s1 = {1,2,3}
s2 = s1

def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)  # 绑定一个删除对象时的回调函数

# s1和s2引用同一个对象。对象的引用计数为0时，输出Gone with the wind...
print(ender.alive)      # True
del s1
print(ender.alive)      # True
s2 = "new obj"          # Gone with the wind...
print(ender.alive)      # False
