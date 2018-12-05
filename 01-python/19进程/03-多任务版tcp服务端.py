import threading
import socket


# 接收客户端消息的函数
def recv_client_data(service_client_socket, ip_port):
    # 循环接收客户端发送的消息
    while True:
        recv_data = service_client_socket.recv(1024)
        if recv_data:
            # 对二进制数据进行解码
            recv_content = recv_data.decode("gbk")
            print(ip_port, "接收到的数据为:", recv_content)

            # 发送给客户端数据
            service_client_socket.send("ok...".encode("gbk"))
        else:
            #
            print(ip_port, "客户端下线了")
            break

    # 终止和客户端通信
    service_client_socket.close()


if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置socket选项, 程序退出端口号理解释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 9098))
    # 设置监听
    tcp_server_socket.listen(128)
    # 循环接收客户端的连接请求
    while True:
        # 等待接收客户端连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()
        print(ip_port, "客户端连接成功")

        # 创建子线程
        sub_thread = threading.Thread(target=recv_client_data, args=(service_client_socket, ip_port))
        # 守护主线程
        sub_thread.setDaemon(True)
        # 启动线程
        sub_thread.start()

        # 循环接收客户端发送的消息
        # while True:
        #     recv_data = service_client_socket.recv(1024)
        #     if recv_data:
        #         # 对二进制数据进行解码
        #         recv_content = recv_data.decode("gbk")
        #         print(ip_port, "接收到的数据为:", recv_content)
        #
        #         # 发送给客户端数据
        #         service_client_socket.send("ok...".encode("gbk"))
        #     else:
        #         #
        #         print(ip_port, "客户端下线了")
        #         break
        #
        # # 终止和客户端通信
        # service_client_socket.close()

    # 提示： 服务端的套接字可以不用关
    # 关闭服务端套接字
    tcp_server_socket.close()