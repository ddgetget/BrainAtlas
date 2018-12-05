# 提示： gevent是封装的greenlet， greent封装的是yield
import gevent
import time

from gevent import monkey
# 打补丁，让gevent识别耗时操作（time.sleep, 网络延时， accept， recv），完成协程之间的切换执行
monkey.patch_all()


def work1():
    for i in range(5):
        print("work1...")
        # gevent默认不失败系统的耗时操作
        time.sleep(0.2)
        # gevent.sleep(0.2)

def work2():
    for i in range(5):
        print("work2...")
        time.sleep(0.2)
        # gevent.sleep(0.2)

if __name__ == '__main__':
    # 创建两个协程执行对应的任务
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # # 主线程等待协程执行完成以后再退出
    # g1.join()
    # g2.join()

    # 提示： 如果gevent没有捕获到耗时操作，那么协程是按照创建顺序依次执行的

    # 提示： 如果主线程执行一个死循环，那么主线程会一直执行，那么这里就不需要加上主线程等待协程执行完成以后再退出程序了
    while True:
        # 提示： 循环里面必须有耗时操作，那么gevent创建的协程才会自动切换执行
        time.sleep(0.2)
        # accept()
        # recv()

