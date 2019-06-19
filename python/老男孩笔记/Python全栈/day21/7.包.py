
# 包:文件夹中有一个__init__.py文件
# 包:是几个模块的集合

# 从包中导入模块
# import
# import glance.api.policy
# glance.api.policy.get()

# import glance.api.policy as policy
# policy.get()

# from import
# from glance.api import policy
# policy.get()

# from glance.api.policy import get
# get()

# 直接导入包
# 绝对导入:
# 在执行一个py脚本的时候,这个脚本以及和这个脚本同级的模块中只能用绝对导入
# 缺点:
    # 所有的导入都要从一个根目录下往后解释文件夹之间的关系
    # 如果当前导入的包的文件和被导入的包的位置关系发生变化,那么所有的init文件都要做相应的调整
# import glance
# glance.api.policy.get()

# 导入一个包
    # 不意味着这个包下面的所有内容都是可以被使用的
    # 导入一个包发生了什么?
        # 相当于执行了这个包下面的__init__.py文件


# 相对导入
# 不需要去反复的修改路径
    # 只需一个包中的所有文件夹和文件的相对位置不发生改变
    # 也不需要去关心当前这个包和被执行的文件之间的层级关系
# 缺点:
# 含有相对导入的py文件不能被直接执行
# 必须放在包中被导入的调用才能正常的使用
# import glance
# glance.api.policy.get()
