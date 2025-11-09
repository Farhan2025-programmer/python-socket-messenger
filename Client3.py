import time

from Client import SocketClient
from threading import Thread

TestClient = SocketClient('Python_Programmer')
TestClient.server_communicate_TCP_IPV4()
time.sleep(1)
TestClient.start_message_receiving()
# Thread(target=SocketClient.message_receiver, args=(TestClient, ), daemon=True).start()
