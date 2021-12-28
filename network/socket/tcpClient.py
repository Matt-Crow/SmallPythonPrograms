# Matt Crow.
from socket import *
from config import TCP_SERVER_ADDR, BUFFER_SIZE, formatAddr

def startTcpClient():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(TCP_SERVER_ADDR) #2
    print(f'{formatAddr(client.getsockname())} connected to {formatAddr(client.getpeername())}')
    message = input("Enter a sentence: ")
    client.send(message.encode()) #3
    response = client.recv(BUFFER_SIZE).decode() #blocks until #4
    print(f'Server responded with "{response}"')
    client.close()

if __name__ == "__main__":
    startTcpClient()
