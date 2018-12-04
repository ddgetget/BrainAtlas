my_set = {3, 4, 5}

print(my_set, type(my_set))

result = list(my_set)

print(result, type(result))

result = tuple(my_set)

print(result, type(result))


# 把列表转成集合set
result = set([1, 3, 5])
print(result, type(result))

result = set((1, 3, 5))
print(result, type(result))

# 列表和元组之间也可以相互转换
result = list((4, 6))
print(result, type(result))


result = tuple(["哈哈", "呵呵"])
print(result, type(result))