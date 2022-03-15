from network import Network
import pickle
import os

network = Network()
game_running = True


def check_game_over():
    global game_running
    game_status = network.check_game_over()
    if game_status:
        print(game_status)
        game_running = False


def draw_game(arr, player_number):
    os.system('cls')
    print("You are player: ", player)
    print("Shells rotate counter-clockwise")
    print("Your cups are bottom side and your goal is the large cup to the right")
    print("Cup numbers are displayed under the board for convenience")
    print("")
    if player_number == 1:
        print("/---|---|---|---|---|---|---|---\\")
        print("|   | " + str(arr[1][5]) + " | " + str(arr[1][4]) + " | " + str(arr[1][3]) + " | " + str(
            arr[1][2]) + " | " + str(arr[1][1]) + " | " + str(arr[1][0]) + " |   |")
        print("| " + str(arr[1][6]) + " |---|---|---|---|---|---| " + str(arr[0][6]) + " |")
        print("|   | " + str(arr[0][0]) + " | " + str(arr[0][1]) + " | " + str(arr[0][2]) + " | " + str(
            arr[0][3]) + " | " + str(arr[0][4]) + " | " + str(arr[0][5]) + " |   |")
        print("\\---|---|---|---|---|---|---|---/")
        print("      1   2   3   4   5   6   -->")
    else:
        print("/---|---|---|---|---|---|---|---\\")
        print("|   | " + str(arr[0][5]) + " | " + str(arr[0][4]) + " | " + str(arr[0][3]) + " | " + str(
            arr[0][2]) + " | " + str(arr[0][1]) + " | " + str(arr[0][0]) + " |   |")
        print("| " + str(arr[0][6]) + " |---|---|---|---|---|---| " + str(arr[1][6]) + " |")
        print("|   | " + str(arr[1][0]) + " | " + str(arr[1][1]) + " | " + str(arr[1][2]) + " | " + str(
            arr[1][3]) + " | " + str(arr[1][4]) + " | " + str(arr[1][5]) + " |   |")
        print("\\---|---|---|---|---|---|---|---/")
        print("      1   2   3   4   5   6   -->")


player = network.get_player_number()
while game_running:
    print("Waiting for your turn")
    print(network.wait_for_turn())

    #check_game_over()

    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state.gameState, int(player))

    print("It is your turn!")
    player_move = input("Enter next move: ")
    network.take_turn(player_move)

    #check_game_over()

    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state.gameState, int(player))

