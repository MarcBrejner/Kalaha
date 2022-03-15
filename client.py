from Network import Network
import pickle
import os

network = Network()
game_running = True


def draw_game(arr):
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


player = network.get_player_number()
print("You are player: ", player)
while game_running:
    print("Waiting for your turn")
    print(network.wait_for_turn())

    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state.gameState)

    print("It is your turn!")
    player_move = input("Enter next move: ")
    response = network.take_turn(player_move)

    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state.gameState)

