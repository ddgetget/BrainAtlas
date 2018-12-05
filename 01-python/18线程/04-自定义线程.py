import threading
import time


# 自定义线程类
class CustomThread(threading.Thread):

    def __init__(self, num1, num2):
        # 手动调用父类的init方法
        super(CustomThread, self).__init__()
        self.num1 = num1
        self.num2 = num2

    # 任务1
    def task1(self):
        time.sleep(1)
        print("任务1执行完成", self.num1)

    # 任务2
    def task2(self):
        time.sleep(1)
        print("任务2执行完成", self.num2)

    # 如果自定义线程，执行任务同一在run方法里面执行
    def run(self):
        print(threading.current_thread())
        # 通过自定义线程执行对应的任务
        self.task1()
        self.task2()


if __name__ == '__main__':
    custom_thread = CustomThread("李四", "王五")
    # 提示： 启动自定义线程同一使用start方法，start方法是启动线程的入口，start方法内部会自动调用run方法
    custom_thread.start()