import pickle
import random
import os
from network import Network


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
    print("You are player: ", player)
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


def play_random_move():
    return random.randrange(1, 7)


def search_for_best_move():
    pass


def play_best_move():
    search_for_best_move()


def get_and_draw_board():
    global network
    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state, int(player))


player = network.get_player_number()
while game_running:
    print("Btzz.. waiting for turn")
    game_status = network.check_game_status()
    if game_status != your_turn:
        print(game_status)
        break

    get_and_draw_board()

    player_move = play_random_move()
    network.take_turn(str(player_move))

    get_and_draw_board()
