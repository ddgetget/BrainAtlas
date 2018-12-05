import time
import multiprocessing


def work():
    for i in range(5):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=work)
    # 1. 方式1主进程退出子进程销毁
    # 守护主进程，主进程退出子进程直接销毁
    # sub_process.daemon = True
    sub_process.start()

    # 等待子进程执行0.5秒钟
    time.sleep(0.5)
    print("over")
    # 2. 让子进程直接销毁
    sub_process.terminate()



