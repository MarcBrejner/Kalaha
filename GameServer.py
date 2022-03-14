import socket
from _thread import *

host = "127.0.0.1"
port = 13000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    socket.bind((host, port))
except socket.error as e:
    str(e)

socket.listen(2)
print("Server has been started, waiting for players")


def threaded_client(connection, player):
    connection.send(str.encode("Connected"))
    while True:
        try:
            data = connection.recv(2048)
            response = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Receiving: ", data)
                print("Sending: ", response)

            connection.sendall(str.encode(response))
        except:
            break



    print("Lost connection")
    connection.close()


currentPlayer = 0
while True:
    connection, addr = socket.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (connection, currentPlayer))
    currentPlayer += 1
