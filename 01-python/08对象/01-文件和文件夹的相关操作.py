import os
import shutil # 文件及文件夹操作的高级目录


# 创建文件夹
# os.mkdir("AAA")

# os.mkdir("BBB")

# 打开文件写入指定数据
# file = open("AAA/1.txt", "w", encoding="utf-8")
#
# file.write("hello 您好")
#
# file.close()

# 查看操作目录的路径
# current_path = os.getcwd()
# print(current_path)
# # 切换目录
# os.chdir("BBB")
#
#
# current_path = os.getcwd()
# print(current_path)
#
#
# file = open("2.txt", "w", encoding="utf-8")
#
# file.write("hello 您好")
#
# file.close()

# os.rename("AAA", "CCC")


# current_path = os.getcwd()
# print(current_path)
# # 切换目录
# os.chdir("BBB")
#
#
# current_path = os.getcwd()
# print(current_path)
# # 扩展--切换到上一级目录
# os.chdir("..")
#
# os.rename("BBB", "DDD")

# os.rename("1.txt", "111.txt")

# os.chdir("CCC")
# os.rename("1.txt", "111.txt")


# 查看目录下文件信息列表
# file_name_list = os.listdir("DDD")
#
# print(file_name_list, type(file_name_list))

# os.chdir("DDD")
# # 查看当前目录下的文件信息列表
# # file_name_list = os.listdir(".")
#
# # 默认查看的就是当前目录下的文件信息列表
# file_name_list = os.listdir()
#
# print(file_name_list)

# os.remove("111.txt")

# os.mkdir("AA")

# os.rmdir("AA")
# os.rmdir("CCC")


# 扩展-------

# 删除目录及目录里面的所有文件
# shutil.rmtree("CCC")

os.chdir("DDD")

# 获取文件的绝对路径： 从根目录（C, D, E, F）算起的路径
abs_path = os.path.abspath("1.txt")
print(abs_path)

# 获取路径中的文件名
file_name = os.path.basename(abs_path)
print(file_name)


# 获取文件的文件名和后缀

file_name, file_name_extend = os.path.splitext(file_name)

print(file_name, file_name_extend)


