from Client import SocketClient

TestClient = SocketClient(userName='Python_Programmer')
TestClient.server_communicate_TCP_IPV4()
TestClient.send_message('Python_Programmer', "Hi How are you...")
