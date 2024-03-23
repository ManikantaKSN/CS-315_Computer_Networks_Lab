import time
from socket import *

serverName = 'localhost'
serverPort = 12000

#creating UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

total_time = 0
no_of_responses = 0
print('\n----------------------------------------')

# for 10 pings
for i in range(1, 11):
    
    start_time = time.time()
    msg = f'Ping {i} {time.ctime(start_time)}'
    clientSocket.sendto(msg.encode(), (serverName, serverPort))

    try:
        modified_msg, server_addr = clientSocket.recvfrom(1024)
        rtt = time.time() - start_time
        print(f'PING SEQ NO: {i}\nResponse from server: {modified_msg.decode()}')
        print(f'RTT: {rtt} seconds')
        print('----------------------------------------')
        total_time += rtt
        no_of_responses += 1

    except timeout:
        print(f'PING SEQ NO: {i}\nRequest timed out')
        print('----------------------------------------')

packet_loss_rate = (10 - no_of_responses) / 10 * 100
print()
print('Ping Statistics')
print('----------------')
print(f'Packet loss rate: {packet_loss_rate}%')

if no_of_responses > 0:
    avg_rtt = total_time / no_of_responses
    print(f'Average RTT: {avg_rtt} seconds')
    print()
clientSocket.close()