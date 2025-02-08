import socket

server_socket = socket.socket()

HOST_IP = 'localhost'
HOST_PORT = 13456

server_socket.bind((HOST_IP, HOST_PORT))

server_socket.listen(5)

print(f"Server Hosted On {HOST_IP}:{HOST_PORT}")


while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr} established")

    client_socket.send(bytes("Welcome to Aditya's server", "utf-8"))

    client_message = client_socket.recv(1024)

    print(client_message.decode())
