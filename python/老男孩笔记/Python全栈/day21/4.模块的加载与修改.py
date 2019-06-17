
import time
import my_module

# 已经导入的模块发生了修改,是不会被感知到的
# time.sleep(20)
# my_module.read1()

time.sleep(20)
my_module.read1()

# 正常情况不用
import importlib
importlib.reload(my_module)