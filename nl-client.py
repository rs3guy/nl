import os
import socket
import subprocess

HOST = '192.168.1.14'    # The remote host
PORT = 8008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

log = "log:TEST_PROG|This is a log file, baby!"

s.send(log)
s.close()

