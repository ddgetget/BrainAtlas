def fibonacci(num):
    a = 0
    b = 1
    index = 0
    print("---11--")
    while index < num:
        result = a
        a, b = b, a + b
        index += 1
        print("---22--")
        # 提示： 代码执行到yield会暂停，然后把结果返回给外界，下次启动生成器在暂停的位置继续往下执行
        yield result
        print("---33--")
        # 代码执行到return关键字生成器会停止迭代抛出停止迭代的异常
        return "ok"


g = fibonacci(5)

value = next(g)
print(value)

try:
    value = next(g)
    print(value)
except StopIteration as e:
    # 获取return返回的值
    print(e.value)

# yield 和 return的区别
# yield可以返回多次值
# return只能返回一次值，如果在生成器里面还会抛出停止迭代的异常