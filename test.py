import socket
from time import sleep

def server():
    host = socket.gethostname()
    print(host)
    port = 3632

    try:
        server = socket.socket()
        print("Socket created")
    except:
        print("Error")

    server.bind((host, port))
    server.listen(5)
    print("Listening....")
    connected, address = server.accept()
    # print (address)
    # print (connected)
    print("Connected with:", address)

    while True:
        # server.listen(5)
        # connected, address = server.accept()



        message_recv = connected.recv(1024).decode()
        print("Message from Client: ", message_recv)

        if not message_recv:
            break

        # if message_recv == None:
        # break

        message_send = input("Enter Message: ")
        connected.send(message_send.encode())

        #if not server.accept():
            #pass

        #else:
            #connected, address = server.accept()
            #print("Connected with:", address)
            #continue



while True:
    server()
