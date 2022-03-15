import socket
import pickle
from _thread import *

from app.game_controller import GameController
from app.game_model import GameModel
from game_enum import GameEnum

host = "127.0.0.1"
port = 13000
your_turn = str.encode("Your turn")
get_game_state = "getGameState"
player_one_won = "Player one won!"
player_two_won = "Player two won!"
player_number = 1
player_one_connection = None
player_two_connection = None

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    socket.bind((host, port))
except socket as e:
    print(e)

socket.listen(2)

gameController = GameController(GameModel())
print("Server has been started, waiting for players")


def send_game_state(current_player):
    game_model = gameController.model
    data_string = pickle.dumps(game_model)
    send_to_player(data_string, current_player)


def check_command(command, current_player):
    if command == get_game_state:
        send_game_state(current_player)

    elif command.isdigit():
        turn_result = gameController.turn(int(command)-1, current_player-1)
        print(turn_result)
        if turn_result == GameEnum.standard:
            if current_player == 1:
                send_to_player(your_turn, 2)
            else:
                send_to_player(your_turn, 1)

        elif turn_result == GameEnum.extra_turn:
            send_game_state(current_player)
            send_to_player(your_turn, current_player)

        elif turn_result == GameEnum.player_one_win:
            #send_to_player(your_turn, 2)
            #send_to_player(player_one_won, 1)
            #send_to_player(player_one_won, 2)
            pass

        elif turn_result == GameEnum.player_two_win:
            #send_to_player(your_turn, 1)
            #send_to_player(player_two_won, 1)
            #send_to_player(player_two_won, 2)
            pass

        else:
            print("Unknown turn result")


def send_to_player(encoded_data, player):
    if player == 1:
        player_one_connection.sendall(encoded_data)
    else:
        player_two_connection.sendall(encoded_data)


def send_player_number(player):
    send_to_player(str.encode(str(player)), player)


def start_when_player_two_joins(player):
    if player == 2:
        send_to_player(your_turn, 1)


def threaded_client(client_connection, player):
    send_player_number(player)
    start_when_player_two_joins(player)
    while True:
        try:
            command = client_connection.recv(2048).decode()
            print(f"Received command {command} from player {player}")

            if not command:
                print("Disconnected")
                break
            else:
                check_command(command, player)

        except socket as er:
            print(er)
            break

    print("Lost connection")
    client_connection.close()


while True:
    connection, addr = socket.accept()

    if player_number < 3:
        print("Connected to: ", addr)
        start_new_thread(threaded_client, (connection, player_number))
        if player_number == 1:
            player_one_connection = connection
        else:
            player_two_connection = connection

        player_number += 1
    else:
        print("Two players already connected")
        connection.close()



