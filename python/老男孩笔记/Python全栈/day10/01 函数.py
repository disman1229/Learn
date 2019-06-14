
# def yue():
#     print('打开手机')
#     print('打开陌陌')
#     print('搜索一下心仪的对象')
#     print('走吧,出去玩啊')
#     print('出发')
#     return '10086','10010','10000'
# # 多个返回值接收到的是元祖
# ret = yue()
# print(ret)


# def jiafa():
#     a = int(input('数字:'))
#     b = int(input('数字:'))
#     c = a + b
#     return c
# result = jiafa()
# print(result)

# 在函数声明的位置的变量:形参
# def yue(tools):
#     print('打开手机')
#     print('打开%s' % tools)
#     print('搜索一下心仪的对象')
#     print('走吧,出去玩啊')
#     print('出发')
# yue('陌陌')

# 位置参数,当函数的参数很多的时候,必须要记住每一个位置是什么
# 关键字参数,按照形参的名字给形参传值
# def chi(good_food,no_good_food,drink,ice_cream):
#     print(good_food,no_good_food,drink,ice_cream)
# chi("法国大蜗牛","卫龙辣条","大白梨","哈根达斯")