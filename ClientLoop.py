from Network import Network

network = Network()
gameRunning = True

while gameRunning:
    playerMove = input("Enter next move: ")
    response = network.send(playerMove)
    print(response)

        