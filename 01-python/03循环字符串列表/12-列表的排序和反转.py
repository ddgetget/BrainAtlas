my_list = [1, 4, 0, 2]

# 对列表进行反转
my_list.reverse()

print(my_list)

my_list = [1, 4, 0, 2]
# 对列表中的数据进行从小到大的排序
# my_list.sort()
# print(my_list)

# 先排序然后在进行反转
# 提示： sort默认是从小到的排序， reverse：True对排序后的结果进行反转
my_list.sort(reverse=True)

print(my_list)