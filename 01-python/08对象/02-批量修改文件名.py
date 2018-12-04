import os

# 获取文件夹下的文件列表信息
file_name_list = os.listdir("Test")

# 切换目录
os.chdir("Test")

# 遍历文件名列表获取每一个文件名
for file_name in file_name_list:
    # 生成新的文件名
    new_file_name = "[彬哥出品]-" + file_name
    print(new_file_name)
    # 重命名
    os.rename(file_name, new_file_name)

