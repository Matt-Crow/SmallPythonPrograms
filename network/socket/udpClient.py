# Matt Crow
from socket import *
from config import UDP_SERVER_ADDR, BUFFER_SIZE, formatAddr

def startUdpClient():
    client = socket(AF_INET, SOCK_DGRAM)
    message = input("Enter a sentence: ")
    client.sendto(message.encode(), UDP_SERVER_ADDR) #2
    response, serverAddr = client.recvfrom(BUFFER_SIZE) # blocks until 3
    response = response.decode()
    print(f'Server responded with "{response}"')
    client.close()

if __name__ == "__main__":
    startUdpClient()
