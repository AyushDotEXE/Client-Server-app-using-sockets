import socket

def start_client():
    host = '127.0.0.1'
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    while True:
        message = input("You: ")
        client_socket.send(message.encode())
        if message == "file":
 
            data = client_socket.recv(1024).decode()
            if data == "filename":
                file_name = input("Enter filename to send: ")
                client_socket.send(file_name.encode())
                with open(file_name, 'rb') as file:
                    file_data = file.read(1024)
                    client_socket.send(file_data)
                print("File has been sent.")
        else:
            data = client_socket.recv(1024).decode()
            print(f"Server: {data}")

if __name__ == "__main__":
    start_client()
