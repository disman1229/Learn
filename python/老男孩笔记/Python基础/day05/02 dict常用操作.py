dic = {"及时雨":"宋江","小李广":"花荣","黑旋风":"李逵","易大师":"剑圣"}
# print(dic.keys())   # 拿到所有的"key"，返回key的集合，像列表，但是不是列表
# for key in dic.keys():
#     print(key)
#
# print(dic.values())
# for value in dic.values():
#     print(value)
print(dic.items())
for k,v in dic.items():
    print(k,v)