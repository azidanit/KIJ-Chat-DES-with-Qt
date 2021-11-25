import socket
import time
from threading import Thread, Lock

from PySide2.QtCore import QObject, Signal, Slot


class CommunicationTCP(QObject):
    getIncomingConnection = Signal(str)
    getMessageData = Signal(str)
    getAccRSAPubKey = Signal(object)

    def __init__(self):
        super(CommunicationTCP, self).__init__()
        print("COMM : Commumication created")
        self.host = '0.0.0.0'
        self.port = 5556

        self.ip_to_connect = '127.0.0.1'
        self.port_to_connect = 5557

        self.server_thread = None

        self.is_server_running = False
        self.is_server_connected_to_client = False
        self.is_server_allowed_connected_to_client = False

        self.connect_client_thread = None
        self.listen_client_thread = None
        self.is_client_connected_to_server = False
        self.is_client_running = False

        self.counter_timeout = 0

        self.data = None
        self.data_mtx = Lock()
        self.param_mtx = Lock()

        self.initSocketServer()
        self.initSocketClient()
        self.startServer()

        self.public_key_rsa = None
        # self.connectToServer()

    def setPublicKeyRSA(self, pub_rsa_):
        self.public_key_rsa = pub_rsa_

    def initSocketServer(self):
        self.socket_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_tcp_server.settimeout(1)
        # print("COMM : Server binding into port", self.port)
        self.socket_tcp_server.bind((self.host, self.port))

    def initSocketClient(self):
        self.socket_tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_tcp_client.settimeout(2)

    def startServer(self):
        self.server_thread = Thread(target=self.startServerThread)
        self.is_server_running = True
        self.server_thread.start()

    def startServerThread(self):
        print("COMM : SERVER WAITING FOR CONNECTION")
        is_key_sent = False
        while self.is_server_running:
            if self.is_client_connected_to_server:
                time.sleep(1)
                continue
            if not self.is_server_connected_to_client:
                self.initSocketServer()
                try:
                    self.socket_tcp_server.listen()
                    self.conn_tcp, self.addr_tcp = self.socket_tcp_server.accept()
                    print('Connected by', self.addr_tcp)
                    self.is_server_connected_to_client = True
                    self.getIncomingConnection.emit(self.addr_tcp[0])
                    self.sendMessageToClient("RSA_KEY," + str(self.public_key_rsa[0]) + "," + str(self.public_key_rsa[1]))
                except:
                    print("COMM : SERVER Timeout Waiting")
                    self.is_server_connected_to_client = False
                    self.socket_tcp_server.close()
                self.counter_timeout = 0
                time.sleep(0.5)
            else:
                self.data_mtx.acquire()
                data = self.conn_tcp.recv(1024)
                data_plain = data.decode()
                self.data_mtx.release()

                if len(data_plain) > 0:
                    if data_plain[:7] == "RSA_KEY":
                        print("COMM : GOT RSA KEY FROM CLIENT")
                        split_data = data_plain.split(',')
                        self.getAccRSAPubKey.emit(split_data)
                    else:
                        self.getMessageData.emit(data.decode())

                if len(data) <= 0:
                    self.counter_timeout += 1
                    time.sleep(0.1)
                    if self.counter_timeout > 100:
                        self.counter_timeout = 0
                        self.conn_tcp.close()
                        self.is_server_connected_to_client = False
                    continue

                print(data)
                # self.conn_tcp.sendall(data)
                time.sleep(0.05)
        print("COMM : server closed")
        self.socket_tcp_server.close()

    @Slot(str)
    def sendMessage(self, msg):
        pass
        if self.is_server_connected_to_client:
            self.sendMessageToClient(msg)
        elif self.is_client_connected_to_server:
            self.sendMessageToServer(msg)
        else:
            print("NO CONNECTED USER")

    def sendMessageToClient(self, msg):
        print("COMM : SERVER SENDING TO CLIENT FROM GUI", msg)
        # if self.is_server_connected_to_client:
        self.conn_tcp.sendall(msg.encode())
        pass

    def sendMessageToServer(self, msg):
        print("COMM : Client SENDING TO SERVER FROM GUI", msg)
        # if self.is_server_connected_to_client:
        self.socket_tcp_client.sendall(msg.encode())
        # pass

    def listenFromServer(self):
        pass

    def connectToServer(self):
        self.initSocketClient()
        self.connect_client_thread = Thread(target=self.connectToServerThread)
        self.connect_client_thread.start()

    def connectToServerThread(self):
        while not self.is_client_connected_to_server and not self.is_server_connected_to_client:
            try:
                print("COMM : Connecting to Server", self.ip_to_connect, self.port_to_connect)
                self.socket_tcp_client.connect((self.ip_to_connect, self.port_to_connect))
                self.is_client_connected_to_server = True
            except:
                print("COMM : Client gagal Konek ke Server")
                self.is_client_connected_to_server = False
                # self.socket_tcp_client.close()

            if self.is_client_connected_to_server:
                print("COMM : starting listening to server")
                self.startListeningToServer()
                break
            time.sleep(0.1)
        # self.socket_tcp_client.close()

    def startListeningToServer(self):
        self.listen_client_thread = Thread(target=self.startListeningToServerThread)
        self.is_client_running = True
        self.listen_client_thread.start()
        pass

    def startListeningToServerThread(self):
        counter_error = 0
        while self.is_client_running and self.is_client_connected_to_server and not self.is_server_connected_to_client:
            # msg_to_send = "COMM : init conn"
            try:
                # self.socket_tcp_client.sendall(msg_to_send.encode())
                data = self.socket_tcp_client.recv(1024)
                data_plain = (data).decode()
                print('COMM : Received client = ', data_plain)

                if len(data_plain) > 0:
                    if data_plain[:7] == "RSA_KEY":
                        print("GOT RSA KEY FROM SERVER")
                        split_data = data_plain.split(',')
                        self.getAccRSAPubKey.emit(split_data)
                        # self.sendMessageToServer("RSA_KEY," + str(self.public_key_rsa[0]) + "," + str(self.public_key_rsa[1]))
                    else:
                        self.getMessageData.emit(data.decode())
            except:
                counter_error += 1
                if counter_error >= 10:
                    print("COMM : Client ERROR recv")
                    counter_error = 0
                # self.socket_tcp_client.close()
                # self.is_client_connected_to_server = False
                # self.initSocketClient()
                # self.connectToServer()
                # break

            time.sleep(0.05)
        print("COMM : Client closed")
        self.socket_tcp_client.close()

    @Slot(str)
    def changeHostToConnect(self, host_ip):
        self.param_mtx.acquire()
        self.ip_to_connect = str(host_ip)
        print("COMM :", "host ip changed to" ,host_ip)
        self.param_mtx.release()

    @Slot(str)
    def changePortToConnect(self, host_port):
        self.param_mtx.acquire()
        self.port_to_connect = int(host_port)
        print("COMM :", "host port changed to", host_port)
        self.param_mtx.release()

    @Slot(str)
    def changeMyPortToConnect(self, local_port):
        self.param_mtx.acquire()
        self.port = int(local_port)
        print("COMM :", "Local port changed to", local_port)
        self.param_mtx.release()

    def disconnectAllComm(self):
        print("COMM : STOPPING ALL COMM THREAD")
        self.param_mtx.acquire()
        self.is_server_running = False
        self.is_client_running = False
        self.is_client_connected_to_server = False
        self.is_server_connected_to_client = False
        self.param_mtx.release()

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
