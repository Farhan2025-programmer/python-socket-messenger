import socket
from threading import Thread

from pickle import loads

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

TestServer = SocketServer()
TestServer.start_server_TCP_IPV4()
