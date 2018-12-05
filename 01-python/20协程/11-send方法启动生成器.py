def fibonacci(num):
    a = 0
    b = 1
    index = 0

    while index < num:
        result = a
        a, b = b, a + b
        index += 1
        # 提示： 代码执行到yield会暂停，然后把结果返回给外界，下次启动生成器在暂停的位置继续往下执行
        params = yield result
        print(params)
        # 生成器停止迭代
        if params == "ok":
            return


fib = fibonacci(5)
# value = next(fib)
#
# print(value)
#
# value = fib.send("ok")
# print(value)

# 建议： 第一次启动生成器使用next，第二个启动生成器如果需要传入参数使用send方法
value = fib.send(None)
print(value)

value = fib.send("error")
print(value)