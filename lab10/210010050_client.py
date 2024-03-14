import time
from socket import *

serverName = 'localhost'
serverPort = 12000
num_pings = 10

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

total_time = 0
received_responses = 0
print('\n----------------------------------------')

for i in range(1, num_pings + 1):
    
    start_time = time.time()
    message = f'Ping {i} {start_time}'
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        end_time = time.time()
        rtt = end_time - start_time
        print(f'PING {i}\nResponse from server: {modifiedMessage.decode()}')
        print(f'RTT: {rtt} seconds')
        print('----------------------------------------')
        total_time += rtt
        received_responses += 1

    except timeout:
        print(f'PING {i}\nRequest timed out')
        print('----------------------------------------')

packet_loss_rate = (num_pings - received_responses) / num_pings * 100
print('\nPing Statistics')
print('----------------')
print(f'Packet loss rate: {packet_loss_rate}%')
if received_responses > 0:
    avg_rtt = total_time / received_responses
    print(f'Average RTT: {avg_rtt} seconds')
    print()
clientSocket.close()