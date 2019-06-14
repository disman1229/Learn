

import re
# s = '<a>wahaha</a>'
# ret = re.search('<(\w+)>(\w+)</(\w+)>',s)
# print(ret.group())  # 所有的结果
# print(ret.group(1)) # 数字参数代表的是取对应分组中的内容
# print(ret.group(2))
# print(ret.group(3))

# 为了findall也可以顺利取到分组中的内容,有一个特殊的语法,就是优先显示分组中的内容
# ret = re.findall('>(\w+)<',s)
# print(ret)
# ret = re.findall('(\w+)',s)
# print(ret)

# 取消分组优先(?:正则表达式)
# python和正则表达式之间的特殊约定
# ret = re.findall('\d+(?:\.\d+)?','1.234*4.3')
# print(ret)


# 关于分组
# 对于正则表达式来说,有些时候我们需要进行分组,来整体约束某一组字符出现的次数
# (\.[\w+]+)?

# 对于python语言来说,分组可以帮助你更好更精准的找到你真正要的内容


# split
# ret = re.split('\d+','luban34cheng21an89dsa')
# print(ret)
# ret = re.split('(\d+)','luban34cheng21an89dsa')
# print(ret)


# 分组命名  (?P<这个组的名字>\w+) 组名不能用数字
# ret = re.search('>(?P<con>\w+)<',s)
# print(ret)
# print(ret.group(1))
# print(ret.group('con'))


s = '<a>wahaha</b>'

# pattern = '<(\w+)>(\w+)</(\w+)>'
# ret = re.search(pattern,s)
# print(ret.group(1) == ret.group(3))

# 使用前面的分组,要求使用的这个名字的分组和前面同名分组中的内容匹配的必须一致
pattern = '<(?P<tab>\w+)>(\w+)</(?P=tab)>'
ret = re.search(pattern,s)
print(ret)


# 2019-6-5