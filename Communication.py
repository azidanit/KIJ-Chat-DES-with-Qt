import socket
import time
from threading import Thread, Lock

from PySide2.QtCore import QObject, Signal, Slot


class CommunicationTCP(QObject):
    getIncomingConnection = Signal(str)

    def __init__(self):
        print("Commumication created")
        self.host = '127.0.0.1'
        self.port = 5556

        self.ip_to_connect = '127.0.0.1'
        self.port_to_connect = 5557

        self.server_thread = None

        self.is_server_running = False
        self.is_server_connected_to_client = False

        self.connect_client_thread = None
        self.listen_client_thread = None
        self.is_client_connected_to_server = False
        self.is_client_running = False

        self.counter_timeout = 0

        self.data = None
        self.data_mtx = Lock()

        self.initSocket()
        self.startServer()

        self.connectToServer()

    def initSocket(self):
        self.socket_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_tcp_server.settimeout(1)

        self.socket_tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_tcp_client.settimeout(1)

    def startServer(self):
        self.server_thread = Thread(target=self.startServerThread)
        self.is_server_running = True
        self.server_thread.start()

    def startServerThread(self):
        print("WAITING FOR CONNECTION")
        self.socket_tcp_server.bind((self.host, self.port))
        while self.is_server_running:
            if not self.is_server_connected_to_client:
                try:
                    self.socket_tcp_server.listen()
                    self.conn_tcp, self.addr_tcp = self.socket_tcp_server.accept()
                    print('Connected by', self.addr_tcp)
                    self.is_server_connected_to_client = True
                    self.getIncomingConnection.emit(self.addr_tcp)
                except:
                    print("Timeout Waiting")
                    self.is_server_connected_to_client = False
                self.counter_timeout = 0
                time.sleep(0.5)
            else:
                self.data_mtx.acquire()
                data = self.conn_tcp.recv(1024)
                self.data_mtx.release()

                if len(data) <= 0:
                    self.counter_timeout += 1
                    time.sleep(0.1)
                    if self.counter_timeout > 20:
                        self.counter_timeout = 0
                        self.conn_tcp.close()
                        self.is_server_connected_to_client = False
                    continue

                print(data)
                self.conn_tcp.sendall(data)
                time.sleep(0.1)




    def listenFromServer(self):
        pass

    def connectToServer(self):
        self.connect_client_thread = Thread(target=self.connectToServerThread)
        self.connect_client_thread.start()

    def connectToServerThread(self):
        while not self.is_client_connected_to_server and not self.is_server_connected_to_client:
            try:
                self.socket_tcp_client.connect((self.ip_to_connect, self.port_to_connect))
                self.is_client_connected_to_server = True
            except:
                print("Client gagal Konek ke Server")
                self.is_client_connected_to_server = False
                # self.socket_tcp_client.close()

            if self.is_client_connected_to_server:
                self.startListeningToServer()
                break
            time.sleep(0.1)

    def startListeningToServer(self):
        self.listen_client_thread = Thread(target=self.startListeningToServerThread)
        self.is_client_running = True
        self.listen_client_thread.start()
        pass

    def startListeningToServerThread(self):
        while self.is_client_running and self.is_client_connected_to_server and not self.is_server_connected_to_client:
            msg_to_send = "init conn"
            try:
                self.socket_tcp_client.sendall(msg_to_send.encode())
                data = self.socket_tcp_client.recv(1024)
            except:
                print("ERROR send")
                self.socket_tcp_client.close()
                self.is_client_connected_to_server = False
                self.initSocket()
                self.connectToServer()
                break

            print('Received client', (data).decode())
            time.sleep(0.1)

# print("OPENED APP")
# comm = CommunicationTCP()
# while True:
#     pass
#     # print("main thread runnning")
#     time.sleep(1)
    # print("running")
# host = '127.0.0.1'
# port = 5556
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(1)
# s.bind((host, port))
# print("listening")
# s.listen()
# counter_timeout = 0
# conn, addr = s.accept()
#
# print('Connected by', addr)
# while True:
#     # conn, addr = s.accept()
#     data = conn.recv(1024)
#
#     if len(data) <= 0:
#         counter_timeout += 1
#         time.sleep(0.1)
#
#         if counter_timeout > 20:
#             conn.close()
#             # s.bind((host, port))
#             print("WAITING CONN")
#             s.listen(1)
#
#             conn, addr = s.accept()
#
#             # break
#             time.sleep(0.1)
#         continue
#
#     print(data)
#     conn.sendall(data)
#     time.sleep(0.1)