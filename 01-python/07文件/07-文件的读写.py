# 1.创建文件并写入数据

# # 打开文件
# # 1.txt: 表示文件名
# # w: 可写，不能读取数据
# file = open("1.txt", "w")
# # 写入数据
# file.write('hello world')
# # 关闭文件
# file.close()

# 提示写入中文
# 打开文件
# 1.txt: 表示文件名
# w: 可写，不能读取数据，提示如果使用open用w模式那么文件里面的数据会先清空再写入
# encoding="utf-8": 表示指定写入文件数据的编码格式
# file = open("1.txt", "w", encoding="utf-8")
#
# # 查看写入数据的编码格式
# # cp936-> gbk
# print(file.encoding)
#
# # 写入数据
# file.write('信息')
# file.write('嘻嘻嘻')
# file.write('xxxxfsdjkljsdf')
#
# # 不支持读取数据
# result = file.read()
# print(result)
# # 关闭文件
# file.close()


# 2. 打开文件读取数据
# file = open("1.txt", "r", encoding="utf-8")
# file_content = file.read()
# print(file_content)
#
# # r模式不支持希尔数据， r是只能读取数据
# # file.write("fdd")
#
# file.close()


# 3. 保留原有数据进行追加写入数据， a: 如果文件不存在那么会先创建文件然后再打开文件再追加写入，如果文件存在直接打开追加写入
# file = open("2.txt", "a", encoding="utf-8")
#
# file.write("哈哈哈")
# # a:不支持读取数据
# file_content = file.read()
# print(file_content)
#
# file.close()

# **** 默认文件是使用r模式进行操作，默认只能读取数据


# 4. 使用wb方式以二进制方式写入数据
# ValueError: binary mode doesn't take an encoding argument
# 如果是含有b模式那么不需要指定encoding='utf-8',否则在window系统下开发python程序需要中编码格式为utf-8,默认是gbk
# 注意点: 在mac和liunx里面如果不包含b模式，也不需要指定编码格式因为默认是utf-8模式
# file = open("3.txt", "wb")
#
# # 准备写入的数据
# content = "大家好"
#
# # 把字符串进行编码转成二进制数据
# content_data = content.encode("utf-8")
# print(content_data)
# # 写入二进制数据
# file.write(content_data)
#
# file.close()


# 5. 使用rb方式以二进制方式读取数据
# file = open("3.txt", "rb")
#
# # 读取数据
# file_data = file.read()
# print(file_data)
# # 对数据进行解码，把二进制数据解码成为字符串
# file_content = file_data.decode("utf-8")
# print(file_content)
# file.close()

# 6. 使用ab模式追加写入二进制数据

file = open("4.txt", "ab")
my_str = "哈哈哈"
# 编码成为二进制数据
file_data = my_str.encode("utf-8")
# 追加写入二进制数据
file.write(file_data)

file.close()

