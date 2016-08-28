import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8008               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, address = s.accept()
print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))

<<<<<<< HEAD
while Try:
    data = conn.recv(1024)
    if not data: break
    data_type = data[:data.index(':')]
    print(data_type)


conn.close()
