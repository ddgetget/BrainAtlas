import threading
import time

# 定义全局变量
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        print("添加的数据为：", i)
        g_list.append(i)
        time.sleep(0.2)
    print("添加数据完成:", g_list)


# 读取数据的任务
def read_data():
    print("数据为:", g_list)


if __name__ == '__main__':
    # 创建添加数据的线程
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    # 启动线程执行对应的任务
    add_thread.start()

    # 延时等待
    # time.sleep(1.5)
    # 线程等待
    # 主线程等待添加数据的子线程执行完成以后主线程再继续往下执行。
    add_thread.join()

    read_thread.start()

    # 总结： 线程之间共享全局变量