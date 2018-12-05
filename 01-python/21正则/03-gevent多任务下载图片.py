import urllib.request  # 网络请求模块
import gevent
from gevent import monkey

# 让gevent识别耗时操作
monkey.patch_all()


# 根据图片地址下载对应的图片
def download_img(img_url, img_name):
    # 查看当前协程
    print(gevent.getcurrent())
    try:
        # 打开网络资源，获取网络资源数据
        response = urllib.request.urlopen(img_url)
        with open(img_name, "wb") as img_file:
            while True:
                # 循环获取网络中的资源数据
                img_data = response.read(1024)
                if img_data:
                    # 把资源数据写入到指定文件中
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print("网络异常:", e)
    else:
        print(img_name, "下载成功")


if __name__ == '__main__':
    # 准备图片的url地址
    img_url1 = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2694632761,1829179832&fm=27&gp=0.jpg"
    img_url2 = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3151470019,2675542744&fm=27&gp=0.jpg"
    img_url3 = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=4115825325,3478781251&fm=27&gp=0.jpg"
    # 创建协程执行对应的任务
    g1 = gevent.spawn(download_img, img_url1, "1.jpg")
    print(g1)
    g2 = gevent.spawn(download_img, img_url2, "2.jpg")
    print(g2)
    g3 = gevent.spawn(download_img, img_url3, "3.jpg")
    print(g3)

    # 主线程等待所有的协程执行完成以后程序在退出
    gevent.joinall([g1, g2, g3])