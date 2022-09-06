import socket
# Setting up a socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'
# Binding the socket to a port and IP address
s.bind((hostname,port))
print('Listening at {}'.format(s.getsockname()))