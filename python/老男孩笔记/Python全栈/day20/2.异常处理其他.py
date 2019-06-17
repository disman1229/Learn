
# else分支
# try:
#     print('aaa')
#     name
#     [][1]
# except NameError:
#     print('name error')
# except IndexError:
#     print('index error')
# except Exception as e:
#     print('Exception')
# else:   # 当try中的代码不发生异常的时候走 else 分支
#     print('else error')

# finally分支
# try:
#     print('aaa')
#     name
#     [][1]
# except NameError:
#     print('name error')
# except IndexError:
#     print('index error')
# except Exception as e:
#     print('Exception')
# else:   # 当try中的代码不发生异常的时候走 else 分支
#     print('else error')
# finally:    # 无论如何都会被执行
#     print('finally')

# def func():
#     f = open('file')
#     try:
#         while True:
#             for line in f:
#                 if line.startswith('a'):
#                     return line
#     except:
#         print('异常处理')
#     finally:    # 即使return也会先执行finally中的代码
#         f.close()

# try:
#     f = open('www','w')
#     f.read()
# finally:    # 即使遇到报错,程序结束,也会先执行finally中的代码,然后在结束程序
#     f.close()
#     print('文件已经关闭了')

# finally用来回收一些操作系统的资源,数据库连接 打开的文件句柄 网络连接.

# 语法
# try ... except
# try ... except ... else
# try ... finally
# try ... except ...finally
# try ... except ... else ...finally

# 主动抛出异常:是给其他开发者用的
# raise ValueError
# raise ValueError('你写的不对')

# 断言 - 语法
# assert 1==2 # 只能接受一个布尔值,False
# assert 1==1 # 只能接受一个布尔值,True
# print(123456)

# 自定义异常:面向对象之后