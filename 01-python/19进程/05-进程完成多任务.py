import multiprocessing
import time
import os


def dance():
    # 当前的在那个进程执行
    print("11dance:", multiprocessing.current_process())
    # 获取进程的编号,pid
    print("dance pid:", multiprocessing.current_process().pid, os.getpid())
    # 获取子进程对应的父进程的pid
    print("dance ppid:", os.getppid())

    for i in range(5):
        print("跳舞中。。。。")
        time.sleep(0.2)
        # 杀死你
        # 根据进程编号杀死指定进程
        # 1. 进程编号
        # 2. 强制杀死进程
        os.kill(os.getpid(), 9)


def sing():
    # 当前的在那个进程执行
    print("222sing:", multiprocessing.current_process())
    # 获取进程的编号,pid
    print("sing pid:", multiprocessing.current_process().pid)
    # 获取子进程对应的父进程的pid
    print("sing ppid:", os.getppid())
    for i in range(5):
        print("唱歌。。。。")
        time.sleep(0.2)

if __name__ == '__main__':

    # 当前的在那个进程执行
    print("main:", multiprocessing.current_process())
    print("main pid:", multiprocessing.current_process().pid)
    # 创建跳舞子进程
    # group = None, 表示： 进程组现在只能使用None
    # name: 表示进程名， 默认是Process-1, xxxx
    # target: 表示执行的目标函数/方法
    dance_process = multiprocessing.Process(target=dance, name="mydance")
    print("dance_process:", dance_process)
    sing_process = multiprocessing.Process(target=sing, name="mysing")
    print("sing_process:", sing_process)

    # 启动进程执行对应的任务
    dance_process.start()
    sing_process.start()