import socket
from threading import Thread

host = socket.gethostname()
print(host)
port = 3632


s = socket.socket()


print("Socket Created")


s.bind((host, port))


s.listen(5)
print("Listening...")

def server(conn):
    while True:
        conn, address = s.accept()
        print("Connected with:", address)

        message_recv = conn.recv(1024).decode()
        if not message_recv:
            break

    message_send = input("enter message: ")
    conn.send(message_send.encode())



while True:
    server(conn)

    #Thread.start(server(conn))
