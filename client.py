from Network import Network
import pickle

network = Network()
gameRunning = True

while gameRunning:
    print("Waiting for your turn")
    print(network.waitForTurn())
    gameState = pickle.loads(network.getGameState())
    print(gameState)
    print("It is your turn!")
    playerMove = input("Enter next move: ")
    response = network.takeTurn(playerMove)
