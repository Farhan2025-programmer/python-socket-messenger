from Client import SocketClient

TestClient = SocketClient('TwoUSER_Farhan')
TestClient.server_communicate_TCP_IPV4()
TestClient.send_message(message="Hi how are you", toUser='Python_Programmer')
