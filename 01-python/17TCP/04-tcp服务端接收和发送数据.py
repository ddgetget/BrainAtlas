import socket

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置socket选项，程序退出端口号立即释放， 端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(("", 9191))
    # 设置监听，把主动套接字改成被动套接字， 主动套接字表示： 以后可以收发消息，被动套接字只能接收客户端的连接请求不能收发消息
    # 收发消息有服务端返回的新的套接字来进行
    # 128: 最大的等待连接数， 针对是单线程，多任务可以保证同时有多个客户端同时和服务端连接进行通信
    tcp_server_socket.listen(128)
    print("等待客户端的到来")
    # 等待客户端的连接请求
    # 提示： 只要连接建立成功，会返回一个新的套接字，这个套接字专门服务与客户端
    # accept会阻塞代码，表示要等待客户端的连接
    service_client_socket, ip_port = tcp_server_socket.accept()
    print(ip_port)
    # 接收数据
    recv_data = service_client_socket.recv(1024)

    print("数据长度为:", len(recv_data))

    # 解码数据
    recv_content = recv_data.decode("gbk")

    print("接收客户端的数据为:", recv_content)

    # 发送数据
    service_client_socket.send("ok,问题正在处理中...".encode("gbk"))

    # 关闭服务与客户端的套接字, 终止和客户端通信
    service_client_socket.close()

    # 关闭服务端套接字, 服务端不提供建立连接的服务
    tcp_server_socket.close()

