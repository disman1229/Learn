

import os
# path = os.path.abspath('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')
# print(path)

# 能够给能找到的相对路径改成绝对路径
# path = os.path.abspath('1.os模块.py')
# print(path)

# 就是把一个路径分成两段,第二段是一个文件/文件夹
# path = os.path.split('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')
# print(path)
# path = os.path.split('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19')
# print(path)


# ret1 = os.path.dirname('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')
# print(ret1)
# ret2 = os.path.basename('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')
# print(ret2)

# ret = os.path.exists('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')
# print(ret)

# ret1 = os.path.isabs('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')
# ret2 = os.path.isabs('1.os模块.py')
# print(ret1)
# print(ret2)

# print(os.listdir('/Users/zhangjie/Documents/Learn/python/'))

# print(os.path.isdir('/Users/zhangjie/Documents/Learn/python/'))
# print(os.path.isfile('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py'))

# print(os.path.join('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/','1.os模块.py'))

# size = os.path.getsize('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py')   # 查看文件大小
# print(size)
# ret1 = os.path.getsize('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19')
# ret2 = os.path.getsize('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day18')
# ret3 = os.path.getsize('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day17')
# print(ret1,ret2,ret3)


# 使用python代码统计一个文件夹中所有文件的总大小
# 你需要统计文件夹的大小