#!/usr/bin/python
#Server to catch incoming files

import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8008               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, address = s.accept()
print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))

while True:
    data = conn.recv(1024)
    data = data.decode('UTF-8')
    if not data: break
    data_type = data[:data.index(':')]
    if data_type == 'log':
    	log_name = data[data.index(':') + 1 : data.index('|')]
    	log = data[data.index('|') + 1:]
    	print(log_name)
    	print(log)


conn.close()
