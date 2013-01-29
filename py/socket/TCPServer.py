from socket import *
serverPort = 13447
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("server ready")
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode('utf-8')
	print(sentence, addr)
	connectionSocket.send("Server Reply".encode('utf-8'))
	connectionSocket.close()
