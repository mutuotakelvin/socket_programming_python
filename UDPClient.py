import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('The OS assigned the address {} to me'.format(s.getsockname()))
message = input('Input lowercase sentence:')
data = message.encode('ascii')