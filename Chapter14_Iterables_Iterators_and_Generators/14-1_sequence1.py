
# 所有sequences都是iterable。
# 当遍历对象x时，解释器会调用iter(x)

# iter()首先会调用__iter__()
# 如果没有__iter__()，会调用__getitem__()。从索引0依次遍历

# 这也是为什么sequences是iterable的原因。
# 但注意现在的内置sequences都实现了__iter__()，对__getitem__()的支持是后向兼容

# Iterable:
# Any object from which the iter built-in function can obtain an iterator.
#
# Iterator:
# Any object that implement the __next__ no-argument method that returns
# the next item in a series or raises StopIteration when there are no more items.

# Python obtains iterators from iterables.