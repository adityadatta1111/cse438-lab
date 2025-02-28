import socket


def eval_expression(expression):
    try:
        allowed_chars = set("0123456789+-*/ ")
        if not set(expression).issubset(allowed_chars):
            return "Invalid characters in expression"

        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


def start_server(host="127.0.0.1", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")

        client_socket.sendall(
            b"Welcome to the NSU Math Server!\nSend expressions to get results evaluated. Send '0' to exit.\n"
        )

        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data or data == "0":
                print(f"Client {addr} disconnected.")
                break

            print(f"Received: {data}")
            result = eval_expression(data)
            client_socket.sendall(result.encode() + b"\n")

        client_socket.close()


if __name__ == "__main__":
    start_server()
