import socket
import time

# 这个例子如何 处理缓冲
# use header

HEADERSIZE = 10

# https://www.youtube.com/watch?v=Lbfe3-v7yE0
# 这里2个词分别代表  ipv4, TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 主机和端口
s.bind((socket.gethostname(), 1235))

# 5是序列数 ，queue
s.listen(5)

while True:
    # 客户端名称， 客户端的地址
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')

    msg = "Welcome to the server!"
    # 这里对消息数据处理，加入一个头信息（长度）
    msg = (f'{len(msg):<{HEADERSIZE}}' + msg)

    clientsocket.send(bytes(msg, "utf-8"))
    # clientsocket.close()

    # 不断开连接，保持与客户端的对话
    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = (f'{len(msg):<{HEADERSIZE}}' + msg)
        clientsocket.send(bytes(msg, "utf-8"))

