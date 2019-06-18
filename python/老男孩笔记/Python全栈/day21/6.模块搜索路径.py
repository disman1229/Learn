# import calculate
import sys
path = r'D:\Learn\python\老男孩笔记\Python全栈\day21\3.模块的循环引用'
sys.path.append(path)

# 和被当做脚本执行的文件,同目录下的模块,可以被直接导入
# 除此之外其他路径下的模块,在被导入的时候需要自己修改sys.path
import c
