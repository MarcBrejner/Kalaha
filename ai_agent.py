import math
import pickle
import random
import os

from AI.heuristics import heuristics
from network import Network
from AI.evaluator import evaluator
import numpy as np

network = Network()
game_running = True
your_turn = "Your turn"
evaluator = evaluator()


def cell(c):
    if c > 9:
        return str(c)
    else:
        return str(c)+" "


def draw_game(arr, player_number):
    #os.system('cls')
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


def get_child_states(local_game_state):
    child_states = []
    for move in range(6):
        child_state = evaluator.evaluate(local_game_state, move, int(player) - 1)
        child_states.append(child_state)
        #draw_game(local_game_state, 1)
        #draw_game(child_state, 2)
        #print(heuristics(child_state))
    return child_states


def play_random_move():
    return random.randrange(1, 7)


def update_best_score(new_score, best_score, new_move, best_move, is_max):
    if is_max:
        return (new_move, new_score) if new_score > best_score else (best_move, best_score)
    else:
        return (new_move, new_score) if new_score < best_score else (best_move, best_score)


def search_for_best_move(game_state, depth, is_max):
    #print("At depth: ", depth)
    if depth == 0:
        return -20, heuristics(game_state)

    if is_max:
        best_score = -math.inf
    else:
        best_score = math.inf

    best_move = -1
    child_states = get_child_states(game_state)
    for (move, child_state) in enumerate(child_states):
        new_score = search_for_best_move(child_state, depth - 1, not is_max)[1]
        #print(f"New move: {new_move} and new score: {new_score} ")

        best_move, best_score = update_best_score(new_score, best_score, move, best_move, is_max)
        #print(f"Best move: {best_move} and best score: {best_score} ")

    return best_move, best_score


def play_best_move(game_state):
    best_move, best_score = search_for_best_move(game_state, 2, True)
    return best_move


def get_and_draw_board():
    global network
    game_state = pickle.loads(network.get_game_state())
    draw_game(game_state, int(player))
    return game_state


player = network.get_player_number()
while game_running:
    print("Btzz.. waiting for turn")
    game_status = network.check_game_status()
    if game_status != your_turn:
        print(game_status)
        break

    game_state = get_and_draw_board()

    player_move = play_best_move(game_state)
    network.take_turn(str(player_move))

    get_and_draw_board()
