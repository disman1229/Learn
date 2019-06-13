import os # os模块是和操作系统交互的模块

# os.makedirs('dir1/dir2')
# os.mkdir('dir3')
# os.mkdir('dir3/dir4')

# 只能删空文件夹
# os.rmdir('dir3/dir4')
# os.removedirs('dir3/dir4')
# os.removedirs('dir1/dir2')
# print(os.stat('D:\\'))

# print(os.listdir("D:\\"))

# file_lst = os.listdir('D:\\')
# for path in file_lst:
#     print(os.path.join('D:\\',path))

# exec/eval 执行的是字符串数据类型的python代码
# os.system和os.popen是执行字符串数据类型的命令行代码
# os.system('dir')    # 执行操作系统的命令,没有返回值,实际操作/删除一个文件/创建一个文件夹
# ret = os.popen('dir')   # 适合做查看类型的操作
# print(ret.read())

# print(os.getcwd())  # current work dir  当前工作目录

# os.chdir('D:\Learn\python\老男孩笔记\Python基础\day18')    # 切换当前的工作目录