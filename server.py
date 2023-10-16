import socket


def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server Listening...")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode()

        if data == "file":

            client_socket.send("filename".encode())
            file_name = client_socket.recv(1024).decode()
            file_data = client_socket.recv(1024)
            with open(file_name, 'wb') as file:
                file.write(file_data)
            print(f"File received: {file_name}")

        else:
            print(f"Client: {data}")
            message = input("You: ")
            client_socket.send(message.encode())


if __name__ == "__main__":
    start_server()
