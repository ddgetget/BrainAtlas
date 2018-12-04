# 切片： 根据下标的范围获取一部分数据
# 切片的语法格式: 变量名[起始下标（默认0）:结束下标(结束下标不包含):步长(默认是1)]

my_str = "abcdef"
# 提示： 3对应结束下标不包含在内
result = my_str[1:3]
print(result)

result = my_str[1:4]
print(result)

# 步长默认是1
result = my_str[1:4:1]
print(result)

# [0,3) -> 0,1,2
result = my_str[:3]
print(result)

result = my_str[0:3]
print(result)


# -------------特殊的用法--------------
my_str = "abcdef"
# 从倒数第4个数据获取数据到最后
result = my_str[-4:]
print(result)

# 使用负数下标的方式获取bcd
result = my_str[-5:-2]
print(result)

# 获取整个字符串
result = my_str[0:6]
print(result)

# 表示从第一个数据获取的最后一个数据
result = my_str[:]
print(result)

# 修改步长, 步长表示每次给起始下标加上指定的数据
result = my_str[0:5:2]
print(result)

# -1: 步长表示倒着取值
result = my_str[4:0:-1]
print(result)

result = my_str[-2:-6:-1]
print(result)

# 把整个字符串倒着取值
result = my_str[::-1]
print(result)

# 切片范围不对，获取不了数据，但是不会崩溃
result = my_str[3:1:1]
print(result)