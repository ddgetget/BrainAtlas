import greenlet
import time


# 任务1
def task1():
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)
        # 切换到第二个协程执行对应的任务
        g2.switch()


# 任务2
def task2():
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)
        # 切换到第二个协程执行对应的任务
        g1.switch()

if __name__ == '__main__':
    # 创建协程1
    g1 = greenlet.greenlet(task1)
    g2 = greenlet.greenlet(task2)

    # 切换协程执行对应的任务
    g1.switch()