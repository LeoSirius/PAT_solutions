# 这个程序同3-4，不过使用defaultdict。

# defaultdict在遇到一个新的key时，会调用default_factory，生成默认值
# 注意__getitem__才会触发default_factory，dd.get(some_key)不会触发default_factory
# __getitem__在遇到新key是调用__missing__，进而调用default_factory

import sys
import re
import collections

WORD_RE = re.compile('\w+')  # 匹配数字、字母、下划线

# key is word, value is list of (line_no, column_no)
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

# 结果：
# a [(17, 48), (18, 53)]
# Although [(9, 1), (14, 1), (16, 1)]
# ambiguity [(12, 16)]
# and [(13, 23)]
# ...
# you [(14, 54)]

