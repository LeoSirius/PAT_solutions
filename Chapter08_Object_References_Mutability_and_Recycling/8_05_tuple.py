# tuple不变，实际上是指的tuple元素的id不变。

t1 = (1,2,[3,4])
t2 = (1,2,[3,4])

print(t1 == t2)      # True
print(id(t1[-1]))    # 4506538464

t1[-1].append(5)

print(t1 == t2)      # False
print(id(t1[-1]))    # 4506538464