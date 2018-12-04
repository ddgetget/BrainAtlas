# 遍历列表可以使用for、while循环，但是for循环遍历是最简单
my_list = ["西施", "貂蝉", "杨玉环", "王昭君"]

# for name in my_list:
#     print(name)


# 使用while遍历列表数据

# 循环0-3之间下标然后取值
count = len(my_list)
print(count)
index = 0
while index < count:
    # 根据下标取值，要保证下标的合法范围
    result = my_list[index]
    print(result)
    # 获取一个值，下标需要加，然后获取下一个值
    index += 1
