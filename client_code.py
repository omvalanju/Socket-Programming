import socket


def start_client():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8888

    soc.connect((host, port))

    message = input("Enter message:")

    while True:
        soc.sendall(message.encode())

        message = input("Enter message:")


start_client()
