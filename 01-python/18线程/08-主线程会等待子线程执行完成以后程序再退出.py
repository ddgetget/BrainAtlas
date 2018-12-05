import threading
import time


def task():
    while True:
        print("任务执行中。。。")
        time.sleep(0.5)


def task1():
    while True:
        print("任务执行中。。。")
        # 有可能出现误差
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建子线程
    # 1. daemon=True： 表示守护主线程
    sub_thread = threading.Thread(target=task, daemon=True)
    # 设置守护主线程， 主线程退出子线程直接销毁，不再执行对应的代码
    # 2. 设置守护主线程
    # sub_thread.setDaemon(True)

    # 创建子线程
    second_thread = threading.Thread(target=task1, daemon=True)
    second_thread.setDaemon(True)

    sub_thread.start()
    second_thread.start()

    time.sleep(1)
    print("over")
    exit()

    # 总结： 主线程会等待所有的子线程执行完成以后程序再退出
