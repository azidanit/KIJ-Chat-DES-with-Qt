import socket
import time

host = '127.0.0.1'
port = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    ret = False
    try:
        ret = s.connect((host, port))
        ret = True
    except:
        print("Gagal konek")
        ret = False
        pass
    print(ret)
    if ret:
        break
    time.sleep(0.2)


while True:
    msg_to_send = "Init Conn"
    try:
        s.sendall(msg_to_send.encode())
        data = s.recv(1024)
    except:
        print("ERROR send")
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            ret = False
            try:
                s.connect((host, port))
                ret = True
            except:
                print("Gagal konek2")
                ret = False
                pass
            print(ret)
            if ret:
                break
            time.sleep(0.2)

    print('Received client', (data).decode())
    time.sleep(1)
