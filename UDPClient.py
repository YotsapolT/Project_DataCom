from socket import *
serverName = '192.168.1.41'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print('From Server:', modifiedMessage.decode())
# clientSocket.close()