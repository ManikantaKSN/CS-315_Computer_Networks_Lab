from socket import *
from base64 import *
import sys
import ssl

#add in prompt
userEmail = "smtplab23@gmail.com"
userPassword = "lmvgusmmhxkmzoti"
userDestinationEmail = input("Enter Email Destination: ")
userSubject = input("Enter Subject: ")
userBody = input("Enter Message: ")
msg = '{}.\r\n I love computer networks!'.format(userBody)


# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = "smtp.gmail.com"
#Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
#Fill in end


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220': 
	print('220 reply not received from server.') 

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

#account authentication
clientSocket.send("STARTTLS\r\n".encode())
clientSocket.recv(1024)
sslClientSocket = ssl.wrap_socket(clientSocket)
sslClientSocket.send("AUTH LOGIN\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userEmail.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userPassword.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))


# Send MAIL FROM command and print server response.
#Fill in start
mailFrom = f"MAIL FROM: <{userEmail}>\r\n"
sslClientSocket.send(mailFrom.encode())
recv1 = sslClientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    sys.exit(0)
#Fill in end


# Send RCPT TO command and print server response.
#Fill in start
rcptTo = f"RCPT TO: <{userDestinationEmail}>\r\n"
sslClientSocket.send(rcptTo.encode())
recv1 = sslClientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    sys.exit(0)
#Fill in end


# Send DATA command and print server response.
#Fill in start
dataCMD = "DATA\r\n"
sslClientSocket.send(dataCMD.encode())
recv1 = sslClientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '354':
    print('354 reply not received from server.')
    sys.exit(0)
#Fill in end


# Send message data.
#Fill in start
sslClientSocket.send(msg.encode())
#Fill in end


# Message ends with a single period.
#Fill in start
sslClientSocket.send("\r\n.\r\n".encode())
recv1 = sslClientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    sys.exit(0)
#Fill in end


# Send QUIT command and get server response.
#Fill in start
quitCMD = "QUIT\r\n"
sslClientSocket.send(quitCMD.encode())
recv1 = sslClientSocket.recv(1024).decode() 
print(recv1)
clientSocket.close()
sslClientSocket.close()
if recv1[:3] != '221':
    print('221 reply not received from server.')
    sys.exit(0)
#Fill in end