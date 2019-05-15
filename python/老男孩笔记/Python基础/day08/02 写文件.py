
# 带w的,只要你操作了,就会清空源文件
# 如果文件不存在,会自动创建文件
# f = open("写1.txt",mode="w",encoding="utf-8")
# f.write("沙谷地2.txt")
# f.flush()
# f.close()


# a模式
# 写的时候,换行需要手动操作
# f = open("写1.txt",mode="a",encoding="utf-8")
# f.write("沙谷地3\n")
# f.write("沙谷地4")
# f.flush()
# f.close()


# rb,wb,ab,bytes 如果处理的是非文本文件,mode里面有如果有b,encoding就不能给
f = open("1.jpg",mode="rb")     # 这里不能写encoding
t = open("./tu/2.jpg",mode="wb")
for line in f:
    t.write(line)
f.close()
t.flush()
t.close()