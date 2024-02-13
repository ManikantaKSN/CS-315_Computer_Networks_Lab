import socket
import random

def client():
    client_name = "Client"
    client_number = random.randint(1, 100)
    server_address = ('localhost', 12345)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        message = f"{client_name},{client_number}"
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print('Received:', data.decode('utf-8'))

if __name__ == "__main__":
    client()