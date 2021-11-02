import socket
import time


host = '127.0.0.1'
port = 5557

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(1)
s.bind((host, port))
print("listening")
s.listen()
counter_timeout = 0
conn, addr = s.accept()

print('Connected by', addr)
while True:
    # conn, addr = s.accept()
    data = conn.recv(1024)

    if len(data) <= 0:
        counter_timeout += 1
        time.sleep(0.1)

        if counter_timeout > 20:
            conn.close()
            # s.bind((host, port))
            print("WAITING CONN")
            s.listen(1)

            conn, addr = s.accept()

            # break
            time.sleep(0.1)
        continue

    print(data)
    conn.sendall(data)
    time.sleep(0.1)