import socket


def start_client(host="127.0.0.1", port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    welcome_message = client_socket.recv(1024).decode()
    print(welcome_message.strip())

    while True:
        expression = input("Enter the expression (or '0' to exit): ").strip()
        client_socket.sendall(expression.encode())

        if expression == "0":
            print("Closing connection.")
            break

        result = client_socket.recv(1024).decode().strip()
        print(f"Result: {result}")

    client_socket.close()


if __name__ == "__main__":
    start_client()
