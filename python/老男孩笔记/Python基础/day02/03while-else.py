count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 5:
        break
else: # while不成立执行
    print("这里是else")