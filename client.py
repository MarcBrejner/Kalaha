from network import Network
import pickle
import os

network = Network()
game_running = True
your_turn = "Your turn"


def cell(c):
    if c > 9:
        return str(c)
    else:
        return str(c)+" "


def draw_game(arr, player_number):
    os.system('cls')
    player_number += 1
    print(f"You are player: {player_number} and it is turn {turn}")
    print("Shells rotate counter-clockwise")
    print("Your cups are bottom side and your goal is the large cup to the right")
    print("Cup numbers are displayed under the board for convenience")
    print("")
    if player_number == 1:
        print("/---|---|---|---|---|---|---|---\\")
        print("|   | " + cell(arr[1][5]) + "| " + cell(arr[1][4]) + "| " + cell(arr[1][3]) + "| " + cell(
            arr[1][2]) + "| " + cell(arr[1][1]) + "| " + cell(arr[1][0]) + "|   |")
        print("| " + cell(arr[1][6]) + "|---|---|---|---|---|---| " + cell(arr[0][6]) + "|")
        print("|   | " + cell(arr[0][0]) + "| " + cell(arr[0][1]) + "| " + cell(arr[0][2]) + "| " + cell(
            arr[0][3]) + "| " + cell(arr[0][4]) + "| " + cell(arr[0][5]) + "|   |")
        print("\\---|---|---|---|---|---|---|---/")
        print("      1   2   3   4   5   6   -->")
    else:
        print("/---|---|---|---|---|---|---|---\\")
        print("|   | " + cell(arr[0][5]) + "| " + cell(arr[0][4]) + "| " + cell(arr[0][3]) + "| " + cell(
            arr[0][2]) + "| " + cell(arr[0][1]) + "| " + cell(arr[0][0]) + "|   |")
        print("| " + cell(arr[0][6]) + "|---|---|---|---|---|---| " + cell(arr[1][6]) + "|")
        print("|   | " + cell(arr[1][0]) + "| " + cell(arr[1][1]) + "| " + cell(arr[1][2]) + "| " + cell(
            arr[1][3]) + "| " + cell(arr[1][4]) + "| " + cell(arr[1][5]) + "|   |")
        print("\\---|---|---|---|---|---|---|---/")
        print("      1   2   3   4   5   6   -->")


def get_turn_from_user(game_state):
    global player
    while True:
        player_move = input("Enter next move: ")
        if player_move.isdigit() and 0 < int(player_move) < 7:
            if game_state[int(player)][int(player_move)-1] == 0:
                print("There are no shells in the chosen move, please pick another")
                continue
            return player_move
        print("Invalid move, write a number between 1 and 6")


def get_and_draw_board():
    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state, int(player))
    return game_state


player = int(network.get_player_number()) - 1 #Either 0 or 1
turn = 0
while game_running:
    print("Waiting for your turn...")
    game_status = network.check_game_status()
    if game_status != your_turn:
        print(game_status)
        break

    game_state = get_and_draw_board()

    print("It is your turn!")
    player_move = get_turn_from_user(game_state)
    network.take_turn(player_move)

    get_and_draw_board()
    turn += 1

