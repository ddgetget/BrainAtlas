# file = open("1.txt", "a", encoding="utf-8")
# print(file.encoding)
#
# file.write("哈哈哈哈")
#
# file.close()

# 提示： 关闭文件的操作不用程序员来做了， 由系统（python解释器）来做
with open("2.txt", "w", encoding="utf-8") as file: # file表示打开文件的对象
    file.write("嘻嘻嘻")