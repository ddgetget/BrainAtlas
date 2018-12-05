import socket
import threading


# 发送消息
def send_msg(current_socket):
    # 接收用户发送的数据
    send_content = input("请输入您要发送的内容:")
    # 对字符串进制编码转成二进制数据
    send_data = send_content.encode("gbk")

    # 发送消息
    current_socket.sendto(send_data, ("192.168.167.94", 8080))


# 接收消息
def recv_msg(current_socket):
    while True:
        # 接收数据
        recv_data, ip_port = current_socket.recvfrom(1024)
        # 对二进制数据进程解码转成字符串
        recv_content = recv_data.decode("gbk")
        print("接收的数据为:%s" % recv_content, ip_port)


if __name__ == '__main__':
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口号
    udp_socket.bind(("", 9090))

    # 创建子线程，专门负责接收对方消息的功能
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))
    # 设置守护主线程
    recv_thread.setDaemon(True)
    # 启动子线程
    recv_thread.start()

    while True:
        # 接收用户输入的功能选项
        menu_option = input("0: 退出 1. 发送 ")
        # ctr + y 删除光标所在行
        if menu_option == "1":
            # 发送消息
            send_msg(udp_socket)

        elif menu_option == "0":
            # 跳出循环，以后不再发送和接收消息了
            break

    # 关闭套接字
    udp_socket.close()
