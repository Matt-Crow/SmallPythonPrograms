# Matt Crow.
from socket import *
from config import TCP_SERVER_ADDR, BUFFER_SIZE, END, formatAddr

def startTcpServer():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(TCP_SERVER_ADDR)
    server.listen(1) #1
    end = False
    print(f'TCP server started on {formatAddr(server.getsockname())}')
    while not end:
        clientSocket, clientAddr = server.accept() # blocks until #2
        message = clientSocket.recv(BUFFER_SIZE).decode() # blocks until #3
        print(f'received "{message}" from {formatAddr(clientAddr)}')
        if message == END:
            end = True
            clientSocket.send("bye".encode())
        else:
            clientSocket.send(message.upper().encode()) #4
        clientSocket.close()
    server.close()

if __name__ == "__main__":
    startTcpServer()
