import socket
import os

host_ip = '192.168.0.194'
port_no = 6789
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, port_no))
print(f"Server socket listening on {host_ip}:{port_no}")

while True:
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    request = conn.recv(1024).decode('utf-8')
    
    if request:
        request_parts = request.split()
        method = request_parts[0]
        filename = request_parts[1][1:]

        if not os.path.exists(filename):
            print("Response to client: 404 Not Found")
            response= "HTTP/1.1 404 Not Found\n\n<h1>404 Not Found</h1>"
        else:
            fl = open(filename, 'r')
            content = fl.read()
            print("Response to client: 200 OK")
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {len(content)}\n\n{content}"
        conn.sendall(response.encode('utf-8'))