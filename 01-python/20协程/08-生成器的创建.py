# 生成器是一个特殊的迭代器，可以使用next和for取值

my_list = [i * 2 for i in range(3)]
print(my_list)


# 生成器
g1 = (i * 2 for i in range(3))
print(g1)

# 获取生成器中的值
# value = next(g1)
#
# print(value)

for value in g1:
    print(value)