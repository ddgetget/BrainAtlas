# 1. 函数名不能相同，不支持函数的重载

print("xxx")
def show():
    print("哈哈")



def show(info):
    print(info)


# 如果函数名相同，只能使用最后一个定义的函数
# show('嘻嘻')
# 代码执行到此，说明show是一个函数，函数名保存的是函数再内存中的地址
print("show函数内存地址:", id(show))

# 扩展-> 变量可以保存函数
# 定义变量
func_name = show
print("func_name:", id(func_name))
func_name('哈哈，我还可以这样玩')




# 2. 变量名不能和函数名相同
show = 10
print(id(show))
# 代码执行到此，说明show原来是函数，现在show是一个变量保存的是数据10在内存中的地址
show('哈哈')