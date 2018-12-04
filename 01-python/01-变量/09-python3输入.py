# 输入-》接收用户输入给程序的数据，在python3里面使用input函数
# 使用变量保存用户输入的数据

msg = input("请求输入数据:")
# 总结: input函数返回的数据类型是字符串(str)
# python3里面没有raw_input
print(msg, type(msg), sep="$")
