import socket
import pickle
from _thread import *

from app.game_controller import GameController
from app.game_model import GameModel

host = "127.0.0.1"
port = 13000
your_turn = str.encode("Your turn")
get_game_state = "getGameState"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    socket.bind((host, port))
except socket as e:
    print(e)

socket.listen(2)

gameController = GameController(GameModel())
print("Server has been started, waiting for players")


def check_command(command, current_player):
    if command == get_game_state:
        game_model = gameController.model
        data_string = pickle.dumps(game_model)
        send_to_player(data_string, current_player)

    elif command.isdigit():
        turn_result = gameController.turn(int(command)-1, current_player-1)

        if turn_result == standard:
            if current_player == 1:
                send_to_player(your_turn, 2)
            else:
                send_to_player(your_turn, 1)
        elif turn_result == extra_turn:
            send_to_player(your_turn, current_player)
        elif turn_result == player_one_win:
            pass
        elif turn_result == player_two_win:
            pass
        else:
            print("Unknown turn result")


def send_to_player(encoded_data, player):
    if player == 1:
        playerOneConnection.sendall(encoded_data)
    else:
        playerTwoConnection.sendall(encoded_data)


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

        except socket.error as er:
            print(er)
            break

    print("Lost connection")
    client_connection.close()


currentPlayer = 1
playerOneConnection = None
playerTwoConnection = None
while True:
    connection, addr = socket.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (connection, currentPlayer))

    if currentPlayer == 1:
        playerOneConnection = connection
    else:
        playerTwoConnection = connection

    currentPlayer += 1

    if currentPlayer == 2:
        break
