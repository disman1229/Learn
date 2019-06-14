

# count = 1
# def func():
#     global count
#     print("鲁班七号" + str(count))
#
#     count +=1
#     func()
# func()

# 遍历/Volumes/扩展盘/网站css文件夹,打印出所有的文件和普通文件的文件名

# 递归遍历某个文件夹下所有的文件
import os
def func(filepath,n):
    files = os.listdir(filepath)    # 查案当前文件的目录
    for file in files:  # 获取每一个文件名
        # 获取文件路径
        file_p = os.path.join(filepath,file)
        if os.path.isdir(file_p):   # 判断file是否是一个文件夹
            print("\t"*n,file)
            func(file_p,n+1)
        else:
            print("\t"*n,file)
func("/Volumes/扩展盘/网站css",0)