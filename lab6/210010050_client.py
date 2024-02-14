import socket
import random

target_host_ip = '192.168.0.194'
target_port_no = 6789
client_name = "210010050_client"
client_number = random.randint(1, 100)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host_ip, target_port_no))
message = f"{client_name},{client_number}"
client.sendall(message.encode('utf-8'))
response = client.recv(1024)

if response:
    data = response.decode('utf-8').split(",")
    print('Server response received...')
    print()
    print("Server name:", data[0])
    print("Server number:", data[1])
    print()
else:
    print("No response from server")