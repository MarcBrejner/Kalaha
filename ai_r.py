import math
import pickle
import random
import os
import sys
import time

from AI.heuristics import heuristics
from network import Network
from AI.evaluator import evaluator
import numpy as np

network = Network()
game_running = True
your_turn = "Your turn"
evaluator = evaluator()
pruning = sys.argv[1] if len(sys.argv) > 1 else 0


def cell(c):
    if c > 9:
        return str(c)
    else:
        return str(c)+" "


def draw_game(arr, player_number):
    #os.system('cls')
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


def play_random_move(state):
    while True:
        move = random.randrange(0, 6)
        if state[int(player)][int(move)] != 0:
            break
        else:
            continue
    return move


def get_and_draw_board():
    global network
    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state, int(player))
    return game_state


player = int(network.get_player_number()) - 1
turn = 0
is_maximizing_player = True if player == 0 else False
while game_running:
    print("Btzz.. waiting for turn")
    game_status = network.check_game_status()
    if game_status != your_turn:
        print(game_status)
        break

    game_state = get_and_draw_board()

    player_move = play_random_move(game_state)
    print(f"Player move = {player_move}")
    network.take_turn(str(player_move))

    get_and_draw_board()
    turn += 1
