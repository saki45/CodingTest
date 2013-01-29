from socket import *
serverPort = 13446
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("server ready")
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print(message.decode('utf-8'), clientAddress)
	modifiedMessage = "server reply".encode('utf-8')
	serverSocket.sendto(modifiedMessage, clientAddress)
