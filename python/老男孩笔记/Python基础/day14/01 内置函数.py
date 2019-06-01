

lst = ["鲁班七号","程咬金","花木兰","后裔"]

# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

it = iter(lst)  # 内部封装的就是__iter__()
print(it.__next__())
print(next(it)) # 内部封装的是__next__()