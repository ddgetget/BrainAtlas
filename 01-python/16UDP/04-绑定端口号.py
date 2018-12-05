import socket

if __name__ == '__main__':

    # 创建udp传输协议的socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口号，以后程序启动就使用这个端口号，不会发送变化
    # udp_socket.bind(("192.168.167.135", 9090))
    # 为了兼容有多个网卡的情况，这里的ip地址不指定，相当于向本机的任意一个ip发送数据都能收到
    udp_socket.bind(("", 9090))
    # 发送数据
    udp_socket.sendto("哈哈".encode("gbk"), ("192.168.167.133", 9090))

    # 接收数据
    recv_data, ip_port = udp_socket.recvfrom(1024)
    # 解码二进制数据
    recv_content = recv_data.decode("gbk")
    print("接收的内容:", recv_content, "对方的ip地址:", ip_port)

    # 关闭套接字
    udp_socket.close()