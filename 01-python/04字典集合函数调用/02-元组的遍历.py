# for循环遍历元组
my_tuple = ('苹果', '香蕉', '鸭梨')

for value in my_tuple:
    print(value)

print("--------------")
index = 0
while index < len(my_tuple):
    # 根据下标获取元组中的数据
    value = my_tuple[index]
    print(value)
    index += 1