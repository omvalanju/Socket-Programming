import socket
from threading import Thread

def client_thread(connection):
    while True:
        message_recv = connection.recv(1024)
        print("Message from client: ", message_recv)

        #connected, address = server.accept()
        #print("Connected with:", address)

        #message_send = input("Enter Message: ")
        #connection.send(message_send.encode())

        break


def server():
    # host = "127.0.0.1"
    # print(host)
    port = 3631

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")

    server.bind(('', port))
    server.listen(5)
    print("Listening....")
    #connected, address = server.accept()
    #print("Connected with:", address)

    while True:
        connected, address = server.accept()
        print("Connected with:", address)

        Thread(target=client_thread(connected)).start()


server()
