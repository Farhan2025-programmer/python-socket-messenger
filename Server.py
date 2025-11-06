import socket
from threading import Thread

from pickle import loads

# from PyQt5.QtCore.QTimeZone import kwargs
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 8500))
# server.listen()

class SocketServer:

    def __init__(self, serverIpAddress = '127.0.0.1', serverSocketPortNumber = 8500):
        self.serverIpAddress = serverIpAddress
        self.serverSocketPortNumber = serverSocketPortNumber

    def start_server_TCP_IPV4(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.serverIpAddress, self.serverSocketPortNumber))
        self.server.listen()

        while True:
            self.connection, self.address = self.server.accept()
            Thread(target=self.handler_server_clients, args=(self.connection, self.address)).start()

    def start_server_TCP_IPV6(self):
        self.server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.server.bind((self.serverIpAddress, self.serverSocketPortNumber))
        self.server.listen()

        while True:
            self.connection, self.address = self.server.accept()
            Thread(target=self.handler_server_clients, args=(self.connection, self.address)).start()

    def start_server_UDP_IPV4(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((self.serverIpAddress, self.serverSocketPortNumber))
        self.server.listen()

        while True:
            self.connection, self.address = self.server.accept()
            Thread(target=self.handler_server_clients, args=(self.connection, self.address)).start()

    def start_server_UDP_IPV6(self):
        self.server = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.server.bind((self.serverIpAddress, self.serverSocketPortNumber))
        self.server.listen()

        while True:
            self.connection, self.address = self.server.accept()
            Thread(target=self.handler_server_clients, args=(self.connection, self.address)).start()

    def handler_server_clients(self, connection, address):
        deserializingData = b''
        while True:
            serializedClientData = connection.recv(4096)

            if not serializedClientData:
                break

            deserializingData += serializedClientData

            try:
                deserializedClientData = loads(deserializingData)

                if deserializedClientData.get('HaveFile'):
                    self.get_clients_files(self.connection, deserializedClientData.get('FileName'),
                                           deserializedClientData.get('FileSize'))

                print(deserializedClientData)

                connection.close()
                return deserializedClientData
            except EOFError:
                continue

    def get_clients_files(self, connection, fileName, fileSize):
        connection.send('ok'.encode())

        with open((str(id(connection)) + fileName), 'wb') as file:
            while True:
                clientFile = connection.recv(4096)

                if not clientFile:
                    break

                file.write(clientFile)

            print(f'Received { fileName } file with { fileSize } size.')


# def get_file(connection, fileName, fileSize):
#     print('Here')
#     print(fileName)
#     connection.sendall('ok'.encode())
#     print('Here2')
#
#     with open(('NEW_' + fileName), 'wb') as file:
#         while True:
#             data = connection.recv(1024)
#             if not data:
#                 break
#             file.write(data)
#
#         print('File Recived!')


# def handler_clients(connection, address):
#     while True:
#         data = connection.recv(1024)
#         if not data:
#             print('Closed')
#             break
#
#         deserializedData = loads(data)
#
#         if deserializedData.get('IsFile'):
#             get_file(connection, deserializedData.get('FileName'), deserializedData.get('FileSize'))
#
#     connection.close()

# while True:
#     connection, address = server.accept()
#     Thread(target=handler_clients, kwargs={'connection': connection, 'address': address}).start()

TestServer = SocketServer()
TestServer.start_server_TCP_IPV4()
