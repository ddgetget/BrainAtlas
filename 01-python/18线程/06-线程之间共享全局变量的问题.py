import threading


# 定义全局变量
g_num = 0


# 任务1. 循环1000000次，每循环一次给全局变量加上1
def task1():
    for i in range(1000000):
        global g_num
        g_num += 1

    print("task1:", g_num)


# 任务2. 循环1000000次，每循环一次给全局变量加上1
def task2():
    for i in range(1000000):
        global g_num
        g_num += 1

    print("task2:", g_num)


if __name__ == '__main__':
    # 创建第一个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动线程执行对应的任务
    first_thread.start()

    # 线程等待，主线程等待第一个线程执行完成以后再让第二个线程去执行
    first_thread.join()


    second_thread.start()

    # 线程之间共享全局变量需要注意一个问题，资源竞争，数据错乱的问题，解决办法： 线程等待