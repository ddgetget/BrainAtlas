import socket

# 判断是否是主模块，主要是测试下面的代码是否好用
if __name__ == '__main__':
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置socket选项，开启发送广播消息的功能
    # 1. SOL_SOCKET表示当前套接字
    # 2. SO_BROADCAST表示广播消息的功能选项
    # 3. True: 开启广播
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

    # 发送消息
    # 局域网中的广播地址： 192.168.167.255
    # udp_socket.sendto("大家好，我是大家授课老师，多多关照!".encode("gbk"), ("192.168.167.255", 9090))

    # 通过的广播地址： 255.255.255.255
    udp_socket.sendto("大家好，我是大家授课老师，多多关照!".encode("gbk"), ("255.255.255.255", 9090))

    # 关闭套接字
    udp_socket.close()