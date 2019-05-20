
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

