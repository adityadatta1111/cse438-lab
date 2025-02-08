import socket

client_socket = socket.socket()

SERVER_IP = 'localhost'
SERVER_PORT = 13456

client_socket.connect((SERVER_IP, SERVER_PORT))

message = client_socket.recv(1024)

print(message.decode())


send_message = "Sending from client"
client_socket.send(bytes("Welcome to Aditya's Client", "utf-8"))
