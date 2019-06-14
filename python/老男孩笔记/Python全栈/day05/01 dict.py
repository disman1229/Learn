# dic = {"jay":"周杰伦","jj":"林俊杰","eason":"陈奕迅"}
# print(dic)

# 字典的相关操作
# 增加
# dic = {"jay":"周杰伦"}
# # dic["jj"] = "林俊杰"
# dic.setdefault("eason","陈奕迅")
# print(dic)

# 删除
# dic.pop("jay")    # pop删除，需要输入key值
# dic.popitem()     # popitem 随机删除
# del(dic["jay"])     # del函数删除，直接删除对应的元素
# dic.clear()     # 清空字典
# print(dic)

# 修改
# dic = {"id":1,"name":"李嘉诚","money":1000000}
# # 李嘉诚赔了500
# dic["money"] = dic["money"] - 500
# print(dic)

# 查找
dic = {"及时雨":"宋江","小李广":"花荣","黑旋风":"李逵","易大师":"剑圣"}
# print(dic["易大师是个脑残"])   # 查询key不存在，报错
# print(dic.get("易大师是个脑残","余小c"))   #查询key不存在，返回None，可以传默认值
lst = dic.setdefault("及时雨1","sss")
print(lst)
# 1.首先判断原来的字典中没有这个"key"，如果没有，执行新增
# 2.用这个"key"去字典中查询，返回查询到的结果