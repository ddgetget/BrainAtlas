import sys

# 接收终端启动程序传入的参数
params_list = sys.argv

print(params_list, type(params_list))

# params_list[1]
if len(params_list) >= 2:
    print(params_list[1])


print("哈哈，这是我使用终端方式运行代码")