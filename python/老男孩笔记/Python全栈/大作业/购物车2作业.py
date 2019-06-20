goods = [
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':15},
    {'name':'键盘','price':30},
    {'name':'硬盘','price':399},
    {'name':'内存','price':489},
]


# def login():
#     username = input('请输入账号:')
#     password = input('请输入密码:')
# s = input('请选择你想进行的操作:登录,注册,购物,退出')
# if s == '登录':
#     login()
# elif s == '购物':
#     money = input('请输入金额:')
#     if money.isdigit():
#         money = float(money)

for i in range(len(goods)):
    print(i+1,goods[i])