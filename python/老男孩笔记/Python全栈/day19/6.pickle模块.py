
import pickle

# 1.pickle支持在python中的所有的数据类型
# dic = {(1,2,3):{'a','b'},1:'abc'}
# ret = pickle.dumps(dic)
# print(ret)
# 2.dumps 序列化的结果只能是字节
# print(pickle.loads(ret))
# 3.只能在python中使用
# 4.在和文件操作的时候,需要用rb,wb的模式打开文件
# 5.可以多次dump和多次load
# dump
# with open('pickle_file','wb') as f:
#     pickle.dump(dic,f)

# load
# with open('pickle_file','rb') as f:
#     ret = pickle.load(f)
#     print(ret,type(ret))

# with open('pickle_file','wb') as f:
#     pickle.dump(dic, f)
#     pickle.dump(dic, f)
#     pickle.dump(dic, f)
#     pickle.dump(dic, f)

# with open('pickle_file','rb') as f:
#     while True:
#         try:
#             ret = pickle.load(f)
#             print(ret,type(ret))
#         except EOFError:
#             break
