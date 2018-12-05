import time
import multiprocessing


# 定义全局变量
g_list = list()


# 添加数据
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("add_data:", g_list)


# 读取数据
def read_data():
    print("read_data:g_list:", g_list)


if __name__ == '__main__':
    # 创建添加数据的子进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    # 启动进程
    add_process.start()
    # 主进程等待添加数据进程执行完成以后代码再继续往下执行
    add_process.join()
    read_process.start()

    print("main:", g_list)

    # 进程之间不会共享全局变量，因为进程之间是相互独立的，只不过变量名字相同而已，不是同一个进程里面的变量名
    # 创建子进程其实是主进程的一个副本。