
# *在这里表示的接收位置参数的动态参数,接收到是元祖
# 顺序:位置参数 => *args(arguments) => 默认值
# def chi(name,*food): # 参数名是food   *表示动作传参
#     print(name + "要吃",food)
# chi("disman","盖浇饭","炒饭","火锅")
# chi("disman","大米饭","小米饭")
# chi("disman","馒头")

# 关键字动态传参
# def chi(**food):
#     print(food)
# chi(good_food="狗不理",no_good_food="汉堡",drink="大白梨",ice_cream="巧乐兹")

# 顺序
# 位置参数,*args,默认值参数,**kwargs
# 以上参数可以随意搭配使用


# 单行注释
''' 多行注释 '''
# 函数注释

# def func(a,b):
#     """
#     这个函数是用来计算a和b的和
#     :param a: 第一个数据
#     :param b: 第二个数据
#     :return: 返回两个数的和
#     """
#     return a + b
# print(func.__doc__)  # document文档


# def func(*args,**kwargs):   # *args 相当于一个聚合的作用
#     print(args,kwargs)
#
# func(1,2,3,4,5,a=6,b=7,c=8)

# 形参:聚合
# def func(*food):    # 聚合,位置参数
#     print(food)
# lst = ["鸡蛋","猪蹄","青菜","萝卜"]
# # 实参:打散
# func(*lst)  # 打散,把list,tuple,set,str 进行迭代打散


# 聚合成关键字参数
def func(**kwargs):
    print(kwargs)

dic = {"name":"disman","age":"18"}
func(**dic)     # 打散成关键字参数