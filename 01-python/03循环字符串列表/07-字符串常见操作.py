my_str = "hello"

# 根据字符串查找对应的下标位置
index = my_str.find("e")
print(index)

# 总结： find查找到指定数据返回对应的下标，否则返回-1
index = my_str.find("f")
print(index)

# start: 表示起始下标
# end: 表示结束下标，结束下标不包含
# 在指定范围查找对应的字符串下标
index = my_str.find("o",0,4)
print(index)

# index的使用, 如果找到了指定字符串那么会返回指定字符串的下标，否则崩溃
# index = my_str.index("f")
# print(index)

# start: 表示起始下标
# end: 表示结束下标，结束下标不包含
index = my_str.index("e", 1, 3)
print(index)

# count 统计指定字符串出现的次数
# start: 表示起始下标
# end: 表示结束下标，结束下标不包含
count = my_str.count("l",3, 4)
print(count)

# replace把旧数据替换成新数据
# count: -1 表示全部替换
# count：1 替换一次
result = my_str.replace("l", "w", 1)
print(result)

my_str = "苹果、橘子、西瓜、榴莲"

# 根据指定字符串分割数据
result = my_str.split("、",1)
# maxsplit： -1， 表示全部分割
# maxsplit: 1 表示分割一次
print(result, type(result))


my_str = "hello"
# 判断是否是以指定字符串开头
result = my_str.startswith("h")
print(result)
# 判断是否是以指定字符串结尾
result = my_str.endswith("x")
print(result)

# 在指定字符串长度内居中显示,数据不够补充空格
result = my_str.center(10)
print(result)
# 在指定字符串长度内居左显示，数据不够补充空格
result = my_str.ljust(10)
print(result)
result = my_str.rjust(10)
print(result)

my_str = "   abc   "

print(my_str)
result = my_str.strip()
print(result)

# 扩展-- 默认两边的空白字符，
# -- 去除指定字符
my_str = "&abc&"
result = my_str.strip("&")
print(result)

my_str = "aaabcccs"

# 根据指定字符串，把数据分成三部分以元组方式返回
result = my_str.partition("b")

print(result, type(result))

# join: 根据指定字符串拼接数据
my_flag = '_'
# 拼接字符串数据，前提是每个数据必须是字符串类型
result = my_flag.join("abc")
print(result)

result = my_flag.join(['1','2','4'])
print(result)