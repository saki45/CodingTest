from socket import *
serverName = "localhost"
serverPort = 13446
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'UDP Test'.encode('utf-8')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
