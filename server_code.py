import socket
from threading import Thread


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    host = "127.0.0.1"
    port = 8888

    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")

    soc.bind((host, port))

    soc.listen(5)
    print("listening.....")

    Thread(target=accept_connection().start())
    Thread(target=client_thread(connection).start())

def client_thread(connection):
    while True:

        message_recv = connection.recv(1024)
        print("Message from client: ", message_recv)

def accept_connection():
    while True:
        connection, address = soc.accept()
        print("Connected with ", address)


start_server()
