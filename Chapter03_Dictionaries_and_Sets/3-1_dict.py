# 映射类型要求key是hashable
# hashable的两个必要条件
#    1. hash值在生命周期内不变__hash__()
#    2. hash值能进行比较 __eq__()

# 内建的不可变类型都是hashable。（但是像(1,2,[3,4])是不可hash的，嵌套了list）
# 用户自定义类型默认是可以hash的，hash值就是id()

from collections import abc

print(isinstance({}, abc.Mapping)) # True
