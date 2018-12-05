import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    # 1. AF_INET: ipv4的地址类型
    # 2. SOCK_STREAM： tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口号，提示：客户端不强制绑定端口号，但是服务端一定要绑定端口
    tcp_client_socket.bind(("", 9090))
    # 建立连接, 提示当连接建立成功以后代码才能继续往下执行
    tcp_client_socket.connect(("192.168.167.107", 8080))
    # 发送数据
    tcp_client_socket.send("服务端您好，我是客户端小白!".encode("gbk"))

    # 接收数据
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data)
    # 对二进制数据进行解码
    recv_content = recv_data.decode("gbk")
    print(recv_content)
    tcp_client_socket.close()