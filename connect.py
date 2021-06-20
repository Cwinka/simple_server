import socket


HOST = '127.0.0.1'
PORT = 8080
HEADER = 64

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    while True:
        msg = input("Сообщение: ").encode('utf8')
        ms_ln = str(len(msg)).encode('utf8')
        ms_ln += b' ' * (HEADER - len(ms_ln))

        c.send(ms_ln)
        c.send(msg)

        if not msg: 
            continue

        res_msg = c.recv(512).decode('utf8')
        print(res_msg)
        if res_msg == "Disconnected":
            break
    c.close()