import socket
from pickle import dumps

import os

class SocketClient:

    def __init__(self, serverIpAddress = '127.0.0.1', serverSocketPortNumber = 8500):
        self.serverIpAddress = serverIpAddress
        self.serverSocketPortNumber = serverSocketPortNumber

        self.clientData: dict = {
            'HaveFile': False,
            'FileName': '',
            'FileSize': 0,

            'Message': ''
        }

    def server_communicate_TCP_IPV4(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.serverIpAddress, self.serverSocketPortNumber))

    def server_communicate_TCP_IPV6(self):
        self.client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.client.connect((self.serverIpAddress, self.serverSocketPortNumber))

    def server_communicate_UDP_IPV4(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.connect((self.serverIpAddress, self.serverSocketPortNumber))

    def server_communicate_UDP_IPV6(self):
        self.client = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.client.connect((self.serverIpAddress, self.serverSocketPortNumber))

    def send_message(self, message: any):
        self.clientData['HaveFile'] = False
        self.clientData['Message'] = message

        self.client.send(dumps(self.clientData))
        self.client.close()

    def send_file(self, fileName, message=''):
        with open(fileName, 'rb') as file:

            self.clientData['HaveFile'] = True
            self.clientData['Message'] = message
            self.clientData['FileName'] = file.name
            self.clientData['FileSize'] = os.fstat(file.fileno()).st_size

            self.client.send(dumps(self.clientData))

            serverACK = self.client.recv(4096).decode()

            if serverACK != 'ok':
                self.client.close()
                exit()

            while True:
                clientFile = file.read(4096)

                if not clientFile:
                    break

                self.client.send(clientFile)

        self.client.close()

TestClient = SocketClient()
TestClient.server_communicate_TCP_IPV4()
TestClient.send_file(fileName='architecture.png', message='Here you are')
