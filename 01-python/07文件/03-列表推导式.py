# 列表推导式： 通俗理解就是快速创建（生成）一个列表, 使用for循环快速创建一个列表

my_list = []


for value in range(1, 6):
    my_list.append(value)


print(my_list)


# 列表推导式创建列表
result = [value for value in range(1, 6)]
print(result, type(result))


# 只获取1-5之间的偶数
result = [value for value in range(1, 6) if value % 2 != 0]
print(result, type(result))


result = [[x, y + 1] for x in range(3) for y in range(3)]
print(result, type(result))


result = [(x, y) for x in range(3) for y in range(3)]
print(result, type(result))

# 扩展--
result = [value.count('b') for value in ["abc", "bcd"]]
print(result)