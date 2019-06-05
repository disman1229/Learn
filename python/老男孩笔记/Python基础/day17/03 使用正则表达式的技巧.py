

import re

# ret = re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# 从1-2*(60+(-40.35/5)-(-4*3))中去整数
# print(ret)

# 你要匹配的内容太没有特点了,容易和你不想匹配的内容混在一起
# 怎么精准取到整数,过滤掉小数呢?


ret = re.findall(r"\d+\.\d|\d+","1-2*(60+(-40.35/5)-(-4*3))")
print(ret)

ret = re.findall(r"\d+\.\d|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret)
ret.remove('')
print(ret)