# 元组： 以小括号表现形式的数据集合，元组里面的数据也是任意类型
# 元组的特点： 只能读取数据，不能对数据进行修改(添加、删除、修改这个三个操作是不支持)

my_tuple = (1, 1.15, True, 'hello', [1, 3, 5])

print(my_tuple, type(my_tuple))

# 不能修改元组数据
# my_tuple[0] = 2
# print(my_tuple)

# 不能删除元组数据
# del my_tuple[0]
# print(my_tuple)

# 可以根据下标获取数据
result = my_tuple[-1]

print(result)

result = my_tuple[0]

print(result)

# 使用切片获取一部分数据
result = my_tuple[1:3]
print(result)

# 注意点，如果元组里面只有一个元素，那么需要在元素后面加上逗号

my_tuple = ("xx",)

print(my_tuple, type(my_tuple))