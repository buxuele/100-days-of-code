import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

while True:
    full_msg = ''
    new_msg = True  # a flag

    while True:
        msg = s.recv(16)    # 持续接收数据
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            print("got full msg")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

    # 然后一次性都读出来
    print(full_msg)




