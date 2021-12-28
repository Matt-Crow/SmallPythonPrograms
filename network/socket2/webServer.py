"""
Matt Crow
"""



from socket import *
import os.path
import re



SERVER_HOST = "localhost"
SERVER_PORT = 5139
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)
BUFFER_SIZE = 4096



def startWebServer():
    WebServer(SERVER_ADDR).start()

class WebServer:
    def __init__(self, address):
        self.address = address
        self.server = None
        self.isRunning = False

    def start(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind(self.address)
        self.server.listen(1)
        print(f'Server started on {formatAddr(self.server.getsockname())}')
        self.isRunning = True
        while self.isRunning:
            self.listen()
        self.server.close()

    def listen(self):
        # Step (i): establish connection when contacted by a client
        clientSocket, clientAddr = self.server.accept()

        # Step (ii): receive an HTTP request from the client
        request = clientSocket.recv(BUFFER_SIZE).decode()
        print(f'Received request:\n{request}')

        # Step (iii): determine which file the client is requesting
        requestedFile = self.parseRequest(request)

        # Step (iv): locate the requested file
        response = "\r\n".join([
            "HTTP/1.1 404 Not Found",
            "",
            f'404 Not Found: Failed to locate the resource "{requestedFile}" on the server'
        ])
        resourcePath = self.getResourcePath(requestedFile)
        if resourcePath is not None:
            # Step (v): build a response containing the requested file, if able
            response = self.buildResponseText(resourcePath)
        print(f'Responding with:\n{response}')

        # Step (vi): transmit response
        clientSocket.send(response.encode())

        clientSocket.close() # assignment specifies non-persistent HTTP

        if requestedFile.lower() == "end":
            self.stop()

    def parseRequest(self, request):
        # extracts the requested resource name
        regex = re.match("GET /([^ ]*) HTTP", request)
        ret = ""
        if regex is not None:
            ret = regex.group(1)
        return ret

    def getResourcePath(self, name):
        path = None
        if os.path.isfile(name):
            path = name
        else:
            resourcePath = os.path.join("resources", name)
            if os.path.isfile(resourcePath):
                path = resourcePath
        return path

    def buildResponseText(self, fileName):
        lines = [
            "HTTP/1.1 200 OK"
        ]

        if fileName.endswith(".html"):
            lines.append("content-type: text/html; charset=UTF-8")
        elif fileName.endswith(".json"):
            lines.append("content-type: text/json; charset=UTF-8")
        else:
            lines.append("content-type: text/plain; charset=UTF-8")
        lines.append("")
        f = open(fileName)
        lines.append(f.read())
        f.close()
        return "\r\n".join(lines)

    def stop(self):
        self.isRunning = False

def formatAddr(addr):
    return f'{addr[0]}:{addr[1]}'

if __name__ == "__main__":
    startWebServer()
