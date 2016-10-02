#!/usr/bin/python3

import os
import socket
import subprocess

HOST = '127.0.0.1'    # The remote host
PORT = 8008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

log = "log:TEST_PROG|This is a log file, baby!"

s.send(log.encode())
s.close()
