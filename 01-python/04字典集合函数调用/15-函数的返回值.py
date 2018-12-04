# 定义函数，接收一个数字参数，根据数字参数，返回不同的烟的信息
print("开始定义函数了")

def buy_yan(money):
    if money == 10:
        # print("黄金叶")
        # return的作用就是把结果返回出去，在函数外面使用
        return "黄金叶"
    else:
        return "对不起，钱不够"


# 调用函数
result = buy_yan(10)

print(result)

# 总结： 如果在函数内部有return 参数表示函数有返回值

my_tuple = ('abc',)
result = len(my_tuple)
print(result)