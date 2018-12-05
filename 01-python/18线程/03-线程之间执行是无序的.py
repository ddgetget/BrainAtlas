import threading
import time


def task():
    time.sleep(1)
    print(threading.current_thread().name)
    print("任务执行完成")


if __name__ == '__main__':
    # 循环创建多个子线程
    for i in range(100):
        sub_thread = threading.Thread(target=task)
        print(id(sub_thread))
        sub_thread.start()


    # 总结： 线程之间执行的时候是无序的，由cpu调度决定的
