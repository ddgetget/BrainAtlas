import socket


# 程序入口代码
if __name__ == '__main__':
    # 创建udp传输协议的socket
    # 1. AF_INET: ip地址的类型，ipv4, AF_INET6: ipv6
    # 2. SOCK_DGRAM: udp传输协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_content = "哈哈"
    # 把字符串编码成二进制数据
    # window的网络调试助手使用gbk编码和解码
    # send_data = send_content.encode("gbk")
    # linux的网络调试助手使用utf-8编码和解码
    send_data = send_content.encode("utf-8")

    # 发送数据
    udp_socket.sendto(send_data, ("192.168.167.135", 9090))

    # 关闭套接字
    udp_socket.close()