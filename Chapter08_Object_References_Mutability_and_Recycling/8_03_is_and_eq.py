# python中的变量都是对对象的引用

# python对象三个方面：
# - identity
# - type
# - value

# CPython中id()返回对象的内存地址

# is比较的是id()
# ==比较的是对象的值

leo = {
    'name': 'Leo Sirius',
    'born': 1995,
}

leo2 = leo

fake_leo = {
    'name': 'Leo Sirius',
    'born': 1995,
}

print("leo == fake_leo:  {}".format(leo == fake_leo))  # True
print("leo is fake_leo:  {}".format(leo is fake_leo))  # False
print("leo == leo2:      {}".format(leo == leo2))      # True
print("leo is leo2:      {}".format((leo is leo2)))    # True
