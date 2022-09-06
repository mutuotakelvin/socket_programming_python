import socket

MAX_SIZE_BYTES = 65535 # Maximu size of a UDP datagram

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input a lowercase sentence:')
data = message.encode('ascii')
s.sendto(data,('127.0.0.1',3000))
print('The OS assigned the address {} to me'.format(s.getsockname()))
data, address = s.recvfrom(MAX_SIZE_BYTES)