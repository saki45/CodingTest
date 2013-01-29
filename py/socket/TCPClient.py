from socket import *
serverName = 'localhost'
serverPort = 13447
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = "TCP Test".encode('utf-8')
clientSocket.send(sentence)
rcvsentence = clientSocket.recv(1024).decode('utf-8')
print(rcvsentence)
clientSocket.close()
