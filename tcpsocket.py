import socket

def server_program():
    host = '172.16.31.69'  # your IP address
    port = 5050

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print("Server started... waiting for client...")

    conn, address = server_socket.accept()
    print("Connection from:", address)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From client:", data)

        data = input(" -> ")
        conn.send(data.encode())

    conn.close()


if __name__ == "__main__":
    server_program()
