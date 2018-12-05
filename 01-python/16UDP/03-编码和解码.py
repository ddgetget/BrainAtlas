my_str = "哈哈"

my_data = my_str.encode("utf-8", errors="ignore")

# 拼接二进制数据
my_data += "嘻嘻".encode("gbk")

# result = my_str + my_str
# my_str += my_str
# print(my_str)

print(my_data)

result = my_data.decode("utf-8", errors="ignore")

print(result)