

f = open("沙谷地.txt",mode="r",encoding="utf-8")
for line in f:
    print(line.strip())
f.seek(0)   # 移动到开头  # 字节
for line in f:
    print(line.strip())
print(f.tell())  # 光标位置
f.close()

