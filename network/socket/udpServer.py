# Matt Crow
from socket import *
from config import UDP_SERVER_ADDR, BUFFER_SIZE, END, formatAddr

def startUdpServer():
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(UDP_SERVER_ADDR) #1
    end = False
    print(f'started UDP server at {formatAddr(UDP_SERVER_ADDR)}')
    while not end:
        data, clientAddr = server.recvfrom(BUFFER_SIZE) # blocks until 2
        data = data.decode()
        print(f'received "{data}" from {formatAddr(clientAddr)}')
        if data == END:
            server.sendto("bye".encode(), clientAddr)
            end = True
        else:
            server.sendto(data.upper().encode(), clientAddr) #3
    server.close()

if __name__ == "__main__":
    startUdpServer()
