# 读取源文件的数据
# open("5.txt", "r", encoding="utf-8")

# 为了兼容其它类型文件数据，这里使用rb模式

src_file_name = "5.txt"

src_file = open(src_file_name, "rb")

# 读取原文件中的所有数据
src_file_data = src_file.read()

# 1. 使用切片方式获取文件名

# 2. 使用分割(split)把文件名和后缀进行分割
# file_name, file_extend = src_file_name.split(".")
# print(file_name, file_extend)

# 3. 使用partition按照指定字符串分割三部分
file_name, point_name, extend_name = src_file_name.partition(".")
# 生成目标文件名
dst_file_name = file_name + "[复件]" + point_name + extend_name
print(dst_file_name)

# 打开目标文件写入原文件数据
# 如果想要拷贝到指定目标指定目标路径
dst_file = open("C:\\Users\\Apple\\Desktop\\" + dst_file_name, "wb")
# 写入原文件数据
dst_file.write(src_file_data)
# 关闭目标文件
dst_file.close()
# 关闭原文件
src_file.close()
