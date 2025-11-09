import time

from Client import SocketClient

TestClient = SocketClient('TwoUSER_Farhan')
TestClient.server_communicate_TCP_IPV4()
time.sleep(1)
TestClient.send_message(message="I want to by a physic book", toUser='Python_Programmer')
# TestClient.send_message(message="Hi how are you", toUser='Python_Programmer')
# TestClient.send_message(message="Hi how are you", toUser='Python_Programmer')
