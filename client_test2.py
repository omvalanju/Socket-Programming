import socket

def client():
    host = socket.gethostname()
    port = 3632

    client = socket.socket()
    #client.connect((host, port))



    while True:
        client.connect((host, port))
        message_send = input("Enter Message: ")
        client.send(message_send.encode())

        message_recv = client.recv(1024).decode()
        print("Message from Client: ", message_recv)



client()

