import socket
import os

def handle_request(request):
    request_parts = request.split()
    method = request_parts[0]
    filename = request_parts[1][1:]

    if method != "GET":
        return "HTTP/1.1 501 Not Implemented\n\n<h1>501 Not Implemented</h1>"

    if not os.path.exists(filename):
        return "HTTP/1.1 404 Not Found\n\n<h1>404 Not Found</h1>"

    with open(filename, 'r') as file:
        content = file.read()
        response = f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {len(content)}\n\n{content}"
        return response

def run_server():
    host = 'localhost'
    port = 6789

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        connection, address = server_socket.accept()
        request = connection.recv(1024).decode('utf-8')
        if request:
            response = handle_request(request)
            connection.sendall(response.encode('utf-8'))
        connection.close()

if __name__ == "__main__":
    run_server()