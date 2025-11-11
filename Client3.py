import time

from Client import SocketClient
from threading import Thread

TestClient = SocketClient('Python_Programmer')
TestClient.server_communicate_TCP_IPV4()
# TestClient.start_message_sending(toUser='TwoUSER_Farhan')
# TestClient.start_message_receiving()
# TestClient.send_message(message='Nothing', toUser='TwoUSER_Farhan')
# TestClient.start_message_receiving()
# Thread(target=SocketClient.message_receiver, args=(TestClient, ), daemon=True).start()
