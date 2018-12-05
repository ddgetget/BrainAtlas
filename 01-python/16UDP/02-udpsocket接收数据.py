import socket

if __name__ == '__main__':
    # 创建udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 准备发送的数据
    send_data = "大家好，快下课了，忍忍!!!".encode("gbk")

    # 发送数据
    udp_socket.sendto(send_data, ("192.168.167.133", 9090))

    # 接收数据
    # 每次接收数据的最大字节数： 1024字节
    recv_data, ip_port = udp_socket.recvfrom(1024)
    print(recv_data, ip_port)

    # 解码window网络调试助手发送过来的数据
    recv_content = recv_data.decode("gbk")
    print("接收的数据:", recv_content)

    # 关闭套接字
    udp_socket.close()