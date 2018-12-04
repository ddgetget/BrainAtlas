# 列表的嵌套： 列表里面存储的是列表

# 北方城市列表
north_list = ['北京', '哈尔滨']
# 南方城市列表
south_list = ["上海", "杭州"]

# 中国城市列表
city_list = [north_list, south_list]

print(city_list)

# 获取杭州数据

# 1. 获取南方城市列表数据
north_list = city_list[1]
print(north_list)
# 2. 从南方城市列表获取杭州数据
city_name = north_list[1]
print(city_name)

# 简写方式
result = city_list[1][1]
print(result)