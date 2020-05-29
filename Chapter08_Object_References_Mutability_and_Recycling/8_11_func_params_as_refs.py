# python的函数参数是传的引用。即函数形参是实参的别名

a = 1

def f(x):
    print('id a 2 {}'.format(id(x)))
    x += 1
    print('id a 3 {}'.format(id(x)))

print('a begin = {}'.format(a))
print('id a 1 {}'.format(id(a)))
f(a)
print('id a 4 {}'.format(id(a)))
print('a end = {}'.format(a))


# 内建对象不可变，x += 1创建了一个新的对象
# 可见124都是同一对象的不同引用。a += 1时创建了一个新的对象，并把函数内的a引用到那个对象

# a begin = 1
# id a 1 4534820624
# id a 2 4534820624
# id a 3 4534820656
# id a 4 4534820624
# a end = 1

# list可变，x += [2]不会创建新的对象

b = [1]

def f(x):
    print('id b 2 {}'.format(id(x)))
    x += [2]
    print('id b 3 {}'.format(id(x)))

print('b begin = {}'.format(b))
print('id b 1 {}'.format(id(b)))
f(b)
print('id b 4 {}'.format(id(b)))
print('b end = {}'.format(b))

# b begin = [1]
# id b 1 4535964128
# id b 2 4535964128
# id b 3 4535964128
# id b 4 4535964128
# b end = [1, 2]
