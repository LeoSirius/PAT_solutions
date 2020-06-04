# first-class functions 是 "functions as first-class objects"的缩写

# first-class object 的特点：

# - 在运行时创建
# - 能被赋值给变量或数据结构中的一个元素
# - 能作为函数的参数，能被函数返回

# 高阶函数：参数和返回值是函数的函数
# 典型的高阶函数时map, reduce, filter

def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

res = list(map(factorial, range(11)))
print(res)  # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# 现在一般使用listcomp或genexp代替map, filter。reduce的求和功能用sum取代。
# python2中map, filter返回list。
# python3中map, filter返回generator

l1 = list(map(factorial, range(6)))
l2 = [factorial(n) for n in range(6)]
print(l1)  # [1, 1, 2, 6, 24, 120]
print(l2)  # [1, 1, 2, 6, 24, 120]


# 求基数的阶乘  list(filter(lambda n: n % 2, range(6))) = [1,3,5]
l3 = list(map(factorial, filter(lambda n: n % 2, range(6))))
l4 = [factorial(n) for n in range(6) if n % 2]
print(l3)  # [1, 6, 120]
print(l4)  # [1, 6, 120]