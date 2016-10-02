import os
import socket
import subprocess

cmd = "data"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 8080

s.connect((host,port))
print(s.getpeername())
#s.send(cmd.encode())
