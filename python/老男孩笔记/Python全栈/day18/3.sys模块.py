

import sys

# 1.sys.argv
# print(sys.argv) # argv的第一个参数是python这个命令后面的值
# usr = input('username')
# pwd = input('password')

# usr = sys.argv[1]
# pwd = sys.argv[2]
# if usr == 'disman' and pwd == '123':
#     print('登录成功')
# else:
#     exit()

# 2.sys.path
# print(sys.path)
import re


# 3.sys.modules
# print(sys.modules)  # 是我们导入到内存中的所有模块的名字:这个模块的内存地址

print(sys.modules['re'].findall('\d','asd1233'))