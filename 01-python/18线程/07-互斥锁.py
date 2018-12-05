# 互斥锁: 对共享数据进行锁定，保证同一时刻只能有一个线程去执行，那个线程抢到这个锁，那个线程先去执行，其它线程需要等待
# 提示： 线程把任务执行完成需要把锁释放，让其它线程再去抢这个互斥锁

import threading


# 定义全局变量
g_num = 0

# 创建互斥锁, Lock其实就是变量指向的是函数名
lock = threading.Lock()


# 任务1. 循环1000000次，每循环一次给全局变量加上1
def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("task1:", g_num)
    # 释放锁
    lock.release()


# 任务2. 循环1000000次，每循环一次给全局变量加上1
def task2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("task2:", g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建第一个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动线程执行对应的任务
    first_thread.start()

    second_thread.start()

    # 总结: 互斥锁会保证同一时刻只能有一个线程去执行，提示：多任务瞬间变成单任务，执行效率会下降，但是会保证数据没有问题



