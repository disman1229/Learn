
# 万能异常
# def buy():
#     print('buy')
#     name
# def back():
#     print('back')
#     [][1]
# def show():
#     print('show')
#     1/0
# def main():
#     l = [('购物',buy),('退货',back),('查看订单',show)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         num = int(input('num >>>'))
#         print(l[num - 1])
#         try:
#             func = l[num-1][1]
#             func()
#         except Exception:
#             print('用户在选择了%s操作之后发生了不可知的异常'%l[num-1][0])
# main()

# as语法 能够将常见错误打印出来
# def buy():
#     print('buy')
#     name
# def back():
#     print('back')
#     [][1]
# def show():
#     print('show')
#     1/0
# def main():
#     l = [('购物',buy),('退货',back),('查看订单',show)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         num = int(input('num >>>'))
#         print(l[num - 1])
#         try:
#             func = l[num-1][1]
#             func()
#         except Exception as e:
#             print(e.args,e.__traceback__.tb_lineno,e.__traceback__.tb_frame)
#             print(e)
#             print('用户在选择了%s操作之后发生了不可知的异常'%l[num-1][0])
# main()

# 万能异常,相当于except Exception,如果不打印错误信息可以用这个
# try:
#     name
#     [][1]
#     int('aaa')
# except:
#     print(123)

# 多分支+万能异常:万能异常应该永远放在异常处理最下面
# def buy():
#     print('buy')
#     name
# def back():
#     print('back')
#     [][1]
# def show():
#     print('show')
#     1/0
# def main():
#     l = [('购物',buy),('退货',back),('查看订单',show)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         try:
#             num = int(input('num >>>'))
#             print(l[num - 1])
#             func = l[num-1][1]
#             func()
#         except(ValueError,IndexError):
#             print('您输入的内容不合法')
#         except Exception:
#             print('用户在选择了%s操作之后发生了不可知的异常'%l[num-1][0])
# main()

# try:
#     pass
# except(ValueError,IndexError):
#     print('针对性的处理')
# except Exception as e:
#     print(e)
#     print('通用性的处理')