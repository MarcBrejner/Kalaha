from Network import Network
import pickle
import os

network = Network()
gameRunning = True


def drawGame(arr):
    os.system('clear')
    print("Shells rotate counter-clockwise")
    print("player one is top side, player two is bottom")
    print("Cup numbers are displayed under the board for convenience")
    print("Left large cup indicates player one points, right large cup indicates player two points")
    print("")
    print("/---|---|---|---|---|---|---|---\\")
    print("|   | " + str(arr[0][5]) + " | " + str(arr[0][4]) + " | " + str(arr[0][3]) + " | " + str(
        arr[0][2]) + " | " + str(arr[0][1]) + " | " + str(arr[0][0]) + " |   |")
    print("| 0 |---|---|---|---|---|---| 0 |")
    print("|   | " + str(arr[1][0]) + " | " + str(arr[1][1]) + " | " + str(arr[1][2]) + " | " + str(
        arr[1][3]) + " | " + str(arr[1][4]) + " | " + str(arr[1][5]) + " |   |")
    print("\\---|---|---|---|---|---|---|---/")
    print("      1   2   3   4   5   6")


while gameRunning:
    print("Waiting for your turn")
    print(network.waitForTurn())
    gameState = pickle.loads(network.getGameState())
    drawGame(gameState.gameState)
    print("It is your turn!")
    playerMove = input("Enter next move: ")
    response = network.takeTurn(playerMove)


