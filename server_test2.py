import socket
from threading import Thread

def client_thread(connected):
    message_recv = connected.recv(1024).decode()
    print("Message from Client: ", message_recv)

    message_send = input("Enter Message: ")
    connected.send(message_send.encode())

    #connected, address = server.accept()

def server():
    #print(host)
    #host = socket.gethostbyname()
    port = 3632

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(('', port))
    server.listen(5)
    print("Listening....")


    while True:
        connected, address = server.accept()
        print("Connected with:", address)

        Thread(target=client_thread(connected)).start()


server()
