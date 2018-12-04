
# file = open("5.txt", "rb")
#
# # 如果模式是rb读取数据单位是字节
# # 1：表示一个字节
# # 一个字母在utf-8的编码格式下占用1个字节
# # 一个汉字在utf-8的编码格式下占用3个字节
#
# # 如果是r模式读取数据单位是个数
# # 1: 表示读取一个数据
# file_data = file.read(3)
# print(file_data)
# # print(file_data.decode("utf-8"))
# print(file_data.decode("utf-8"))
#
# file.close()

# 读取源文件的数据
# open("5.txt", "r", encoding="utf-8")

# 为了兼容其它类型文件数据，这里使用rb模式

src_file_name = "5.txt"

src_file = open(src_file_name, "rb")

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

while True:
    # 读取原文件中的所有数据
    src_file_data = src_file.read(1024)
    # if len(src_file_data) > 0:
    #     dst_file.write(src_file_data)
    # else:
    #     break

    if src_file_data:
        dst_file.write(src_file_data)
    else:
        break


# 关闭目标文件
dst_file.close()
# 关闭原文件
src_file.close()
