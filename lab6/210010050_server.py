import socket
import random

host_ip = '192.168.0.194'
port_no = 6789
server_name = "210010050_server"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, port_no))
server_socket.listen(1)
print(f"Server socket listening on {host_ip}:{port_no}")

try:
    while True:
        conn, addr = server_socket.accept()
        data = conn.recv(1024).decode('utf-8')
        if data:
            client_name, client_number = data.split(',')
            client_number = int(client_number)
            server_number = random.randint(1, 100)
            if (client_number > 100 or client_number < 1):
                print("Integer value out-of-range, Server Shutting Down ...")
                server_socket.close()
                break
            else:
                print('Connected to:', addr)
                print()
                print('Client name:', client_name)
                print('Server name:', server_name)
                print()
                print('Client number:', client_number)
                print('Server number:', server_number)
                print('Sum of numbers:', client_number + server_number)
                print()
                response = f"{server_name},{server_number}"
                conn.sendall(response.encode('utf-8'))
except KeyboardInterrupt:
    print("Server Shutting Down ...")
    conn.close()
    pass