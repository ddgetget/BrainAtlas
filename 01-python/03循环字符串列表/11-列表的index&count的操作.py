my_list = ["bcd", "abc", "ccc"]

index = my_list.index("abc")
print(index)

# 根据指定数据获取数据对应的的下标，如果没有找到就直接崩溃，否则返回对应的下标
# index = my_list.index("ddd")
# print(index)

# 统计指定数据在列表中出现的次数
result = my_list.count("dd")
print(result)