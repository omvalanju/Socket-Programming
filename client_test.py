import socket


def client():
    # host = "127.0.0.1"
    port = 3631

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('', port))

    while True:
        message_send = input("Enter Message: ")
        client.send(message_send.encode())

        #message_recv = client.recv(1024).decode()
        #print("Message from Client: ", message_recv)


client()
