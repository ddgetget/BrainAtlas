import time
import threading # 使用线程完成多任务


# 跳舞
def dance():
    print("dance:", threading.current_thread())
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)


# 唱歌
def sing():
    print("sing:", threading.current_thread())
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # # 分别执行对应的任务
    # dance()
    # sing()

    # 获取程序中活动线程的列表
    print("111:", threading.enumerate(), type(threading.enumerate()))

    # 获取当前执行代码的线程
    current_thread = threading.current_thread()
    print("main:", current_thread)
    # 创建跳舞的线程
    # group: 线程组，一般不会使用，使用它这个必须是None
    # target: 执行的目标函数/方法
    # name: 线程的名字, 一般不用设置线程名，使用默认值就可以，默认线程的名字是Thread-1,xxxxx
    #
    dance_thread = threading.Thread(target=dance, name="dance_thread")
    print(dance_thread.name)
    sing_thread = threading.Thread(target=sing, name="sing_thread")
    print(sing_thread.name)

    # 获取程序中活动线程的列表
    print("222:", threading.enumerate(), type(threading.enumerate()))

    # 启动线程
    dance_thread.start()
    sing_thread.start()

    # 获取程序中活动线程的列表
    print("333:", len(threading.enumerate()), type(threading.enumerate()))

    # 扩展：- 获取活动线程的个数
    print("444:", threading.active_count())
    # 提示： 线程只有启动以后才会加入到活动线程的列表里面，当线程执行完成，那么线程就会销毁，在线程活动列表中会移除



