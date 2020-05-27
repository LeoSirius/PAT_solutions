# 这个程序统计一个文本中单词的出现位置，并介绍{}.setdefault的用法

import sys
import re

WORD_RE = re.compile('\w+')  # 匹配数字、字母、下划线

# key is word, value is list of (line_no, column_no)
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # insert key with default value. and return value
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

# 结果：
# a [(17, 48), (18, 53)]
# Although [(9, 1), (14, 1), (16, 1)]
# ambiguity [(12, 16)]
# and [(13, 23)]
# ...
# you [(14, 54)]

