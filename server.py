import socket
import threading

HEADER = 64
HOST = '127.0.0.1'
PORT = 8080
FROMAT = 'utf8'
DISCONNECT_MSG = ':q'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
print(f'[LISTENING ON] {HOST}')

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    connected = True
    while connected:
        ln = conn.recv(HEADER).decode(FROMAT)
        if ln:
            msg = conn.recv(len(ln)).decode(FROMAT)
            if msg == DISCONNECT_MSG:
                conn.send('Disconnected'.encode('utf8'))
                break
            conn.send('Received'.encode('utf8'))
            print(f"[{addr[1]}] {msg}")


    print(f"[{addr}] has just disconnected ")
    conn.close()
    
while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

