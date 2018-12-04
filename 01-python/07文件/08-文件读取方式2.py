# readlines： 按照每行读取数据
# readline： 读取一行数据

# 默认是按照r模式读取数据的
# file = open("5.txt")
# # readline： 读取一行数据
# result = file.readline()
#
# print(result)
#
# file.close()

#
file = open("5.txt", encoding="utf-8")
# 读取每行数据，把数据放入到列表里面
file_content = file.readlines()
print(file_content)
file.close()