

import os
# 打开文件
with open("沙谷地2.txt",mode="r",encoding="utf-8") as f1,\
    open("沙谷地2_副本",mode="w",encoding="utf-8") as f2:
    for line in f1:
        line = line.replace("disman","沙谷地")
        f2.write(line)
# 删除文件
os.remove("沙谷地2.txt")
os.rename("沙谷地2_副本","沙谷地2.txt")