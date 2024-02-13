import socket
import random

def server():
    server_name = "Server"
    server_number = random.randint(1, 100)
    server_address = ('localhost', 12345)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server_address)
        s.listen(1)
        print('Waiting for a connection...')
        connection, client_address = s.accept()

        with connection:
            print('Connected to:', client_address)
            data = connection.recv(1024).decode('utf-8')
            client_name, client_number = data.split(',')
            client_number = int(client_number)
            
            print('Client name:', client_name)
            print('Server name:', server_name)
            print('Client number:', client_number)
            print('Server number:', server_number)
            print('Sum of numbers:', client_number + server_number)

            response = f"{server_name},{server_number}"
            connection.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    server()