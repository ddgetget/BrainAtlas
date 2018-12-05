# 自定义迭代器对象
class Fibonacci(object):

    def __init__(self, num):
        # num:表示生成fibonacci的个数
        self.num = num
        # 记录前面两个值
        self.a = 0
        self.b = 1
        # 记录当前生成数列的下标
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < self.num:

            result = self.a

            self.a, self.b = self.b, self.a + self.b

            # 下标加上
            self.index += 1

            return result
        else:
            raise StopIteration


fib = Fibonacci(5)
# value = next(fib)
#
# print(value)

for value in fib:
    print(value)

# 使用迭代器的好处是：节省内存，获取值没有上限控制


