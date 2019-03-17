import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# while True:
#     # receive 1024 bytes of data
#     # msg = s.recv(1024)
#     msg = s.recv(8)
#     print(msg.decode("utf-8"))

# 改写上面的 处理 大容量的数据，需要缓冲
full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

# 然后一次性都读出来
print(full_msg)


