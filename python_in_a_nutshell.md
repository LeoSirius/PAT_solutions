# python in a nutshell

## Chapter 1 The Python Data Model

- dunder函数是给解释器调用的，自己不要随便调用

## Chapter 2 Sequence

### 序列的分类

按照元素类型：

- 容器序列：可以存放任意类型对象的引用。如list、tuple、collections.deque等
- 扁平序列：只能存放基础类型的值。其实一段连续的内存空间，更接近于c的数组

按照序列本身可变性：

- 不可变序列
- 可变序列：可变序列是不可变序列的子类，多了`__setitem__`, `__delitem__`, `append`, `pop`等方法

### 列表推导和生成器表达式

- 列表推导是直接把元素生成好，放在内存里
- 生成器表达式是惰性的。在使用到相应元素的时候，才会在内存里把那个元素创建出来。

### 元组不仅仅是不可变的序列，一个更重要的作用是作为数据的一条记录

### 不要把可变类型放到不可变序列里做元素。不要把list放到tuple里

## Chapter 3 Dictionaries and Sets

dict和set都是由hash表实现的。他们的key都必须是hashable的，hashable的两个条件

- hash值在生命周期内不变（`__hash__()`）
- hash值能进行比较（`__eq__()`）

内建不可变类型都是hashable的

注意dict和set的key是不可变的，但dict和set对象本身是可变类型

### dict的实现机制

3.6及之前是像下面这样实现的

```python
entries = [
    ['--', '--', '--'],
    ['--', '--', '--'],
    [hash, key, value],
    ['--', '--', '--'],
    ['--', '--', '--'],
]
```

3.7及之后，引入了一个indices列表

```python
indices = [1, None, None, 0, None, None]
# 此时enteies会插入第一个元素
entries = [
    [12343543, 'name', 'leo'],
    [34323545, 'hanmeimei', 'lihua']
]
```

由上可以看出，3.7及以后dict和旧版本dict的区别：

- 新dict是有序的
- 新dict的hash表时密集的

## Chapter 5 First Class Functions

### 函数是对象

`first-class functions`是`functions as first-class objects`的缩写

`first-class objects`的特点：

- 在运行时创建
- 能被赋值给变量
- 能做为函数的参数，能被函数返回

### 高阶函数：以函数为参数，返回函数的函数

### 可调用对象

python中7种可调用对象：

- 用户定义的函数：def或lambda函数
- 内置函数：C实现的函数
- 内置方法：C实现的方法，如dict.get()
- 类
- 类的实例：类定义了`__call__`，则实例可以像函数一样调用
- 方法
- 生成器函数：函数中用yield，返回的是一个生成器对象

## Chapter 7 Function Decorators and Closures

### 装饰器

- 装饰器是语法糖，其本质：一个`以函数为参数`的`可调用对象`
- 装饰器在模块加载的时候，就会执行

### 对一个函数使用多个装饰器，装饰器会从里到外（从上到下）执行

```python
>>> def d1(f):
...     print('in d1')
...     return f
... 
>>> def d2(f):
...     print('in d2')
...     return f
... 
>>> @d1
... @d2
... def f():
...     print('in f')
... 
in d2    # 可以看到先执行了d2，再执行d1
in d1
>>> f()
in f
```

调用的f相当于`f = d1(d2(f))`

### 闭包：一种延伸了作用域的函数

> 在闭包中用nonlocal可以把变量声明为自由变量

```python
>>> def make_averager():
...     series = []
...     
...     def averager(new_value):
...         series.append(new_value)       # 这里的series称为自由变量，这个术语专指未在本地作用域中绑定的变量
...         total = sum(series)
...         return total / len(series)
...     
...     return averager
... 
>>> avg = make_averager()
>>> 
>>> avg(1)
1.0
>>> avg(2)
1.5
>>> avg.__code__.co_varnames   # 显示局部变量
('new_value', 'total')
>>> avg.__code__.co_freevars   # 显示自由变量
('series',)
```

## Chapter 8 Object References Mutability and Recycling

### 变量都是引用

### `==`判断的是对象是值是否相等，`is`判断的是是否是同一个对象
